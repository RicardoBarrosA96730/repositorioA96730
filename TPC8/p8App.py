# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:04:23 2021

@author: User
"""


import PySimpleGUI as sg
import tpc8modulo as tpc

myExameBD = []

sg.theme("BlueMono")

# Painel com duas colunas: 
# Coluna 1: menu
# Coluna 2: Dados

import PySimpleGUI as sg

# Painel com duas colunas: 
# Coluna 1: menu
# Coluna 2: Dados

##juntou as duas, carregando no inserir reg. abre outra janela com um form.

menu_list_column = [
    [sg.Button("Carregar BD de EMDs", font=('Arial', 16))],
    [sg.Button("Listar BD de EMDs", font=('Arial', 16))],
    [sg.Button("Distribuição por Modalidades na BD de EMDs", font=('Arial', 16))],
    [sg.Button("Distribuição por ano de EMDs", font=('Arial', 16))],
    [sg.Button("Distribuição por clube de EMDs", font=('Arial', 16))],
    [sg.Button("Sair", font=('Arial', 16))],
    [sg.Text('_'*30)],
    [sg.Text('EMDs na BD',font=('Arial', 16))],
    [sg.Listbox(values=[], select_mode='extended', key='-Lista-', size=(110,20))]
]

data_viewer_column = [
    [sg.Text("Painel de Dados", font=('Arial', 20))],
    [sg.Text(size=(40, 2), key="-Dados-",font=('Arial', 16))],
]

layout = [
    [
        sg.Column(menu_list_column),
        sg.VSeperator(),
        sg.Column(data_viewer_column),
    ]
]



windowApp = sg.Window("EMD", layout)

eBD= tpc.lerDataset("emd.csv")

stop = False
while not stop:
    event, values = windowApp.read()
    
    if event == "Sair" or event == sg.WIN_CLOSED:
        stop = True
    
    elif event == "Carregar BD de EMDs":  
        #myExameBD= tpc.lerDataset("emd.csv")
        windowApp['-Dados-'].update("Foram carregados " + str(len(eBD)) + " EMDs" )

    elif event == "Listar BD de EMDs":  
        #myExameBD= tpc.lerDataset("emd.csv")
        vista = tpc.listarDataset(eBD)
        windowApp["-Dados-"].Update("Listagem da BD de EMDs...")
        windowApp['-Lista-'].Update(vista)
        
    elif event == "Distribuição por Modalidades na BD de EMDs":
        m = tpc.modalidades(eBD)
        mod = " "
        for i in range(len(m)):
            mod = mod + mod[i] + "\n"
        windowApp["-Dados-"].Update("Modalidades: \n" + mod)
        windowApp["-Dados-"].Update(tpc.plotDistribPorModalidade(eBD))
        
    elif event == "Distribuição por ano de EMDs":
        windowApp["-Dados-"].Update("Ano: \n")
        windowApp["-Dados-"].Update(tpc.plotDistrib(tpc.distribPorAno(eBD)))
    
    elif event == "Distribuição por clube de EMDs":
        windowApp["-Dados-"].Update("Clube: \n")
        windowApp["-Dados-"].Update(tpc.plotDistrib(tpc.distribPorClube(eBD)))
        
        
        
        
    #else:
     #   windowApp["-Dados-"].update("Erro: evento desconhecido :: " + inputEvent)
        


windowApp.close()

