# módulo que implementa leitura, processamento e produção de dados
# estatísticos de um dataset de exames médicos desportivos
#
# O dataset tem a seguinte estrutura:
'''
_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
6045074cd77860ac9483d34e,0,2020-02-25,Delgado,Gay,28,F,Gloucester,BTT,ACRroriz,delgado.gay@acrroriz.biz,true,true
6045074ca6adebd591b5d239,1,2019-07-31,Foreman,Prince,34,M,Forestburg,Ciclismo,ACDRcrespos,foreman.prince@acdrcrespos.org,false,true
6045074c221e2fdf430e9ef0,2,2021-01-06,Cheryl,Berger,21,M,Umapine,Basquetebol,Vitoria,cheryl.berger@vitoria.biz,false,true
6045074c529cbdce549d3923,3,2020-11-19,Graves,Goff,29,F,Babb,Andebol,AVCfamalicão,graves.goff@avcfamalicão.co.uk,false,false
6045074c3319a0f9e79aad87,4,2019-09-01,Mckay,Bolton,29,F,Chilton,Futebol,ACDRcrespos,mckay.bolton@acdrcrespos.me,false,false
6045074c222607e7520ffd24,5,2019-10-07,Marla,Kelley,22,M,Clarence,Atletismo,AmigosMontanha,marla.kelley@amigosmontanha.tv,false,false

...

'''
#
#

# Descreve em texto o teu 
# 
# BdEMD = [EMD]
# EMD = [...]
#
# Leitura/carregamento da informação do ficheiro

def getReg(linha):
    linha1 = linha.replace("\n","")
    reg = linha1.split(",")
    return reg


def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f.readline()
    i=1
    for linha in f:
        linhanova = getReg(linha)
        linhanova = linhanova[1:]
        id = "emd" + str(i)
        linhanova[0] = id
        bd.append(linhanova)
        i = i + 1
    return bd


# Listagem da informação
def chaveOrd(reg):
    return (reg[1])
    
    
def listarDataset(bd):
    print("id   | DataEMD |          Nome         | Resultado ")
    print("__________________________________________________")
    bd.sort(key=chaveOrd, reverse=True)
    for reg in bd:
        string = str(reg[0])+ " | " + str(reg[1])+ " | " + str(reg[2]) + " " + str(reg[3]) + " | " + str(reg[11])            
        print(string)
    return bd


# Consulta de um registo

def consultarDataset(bd, id):
    encontrado = False
    i = 0
    while encontrado == False and i < (len(bd)):
        if bd[i][0] == id:
            #string = ""
            #for elem in bd[i][0]:
             #  string = string+ str(elem)+ "|" 
            #print(string)
            encontrado = True
        else: 
            encontrado = False
            i = i + 1
    if encontrado == True:
        return bd[i]
    else: 
        return encontrado


# o desporto é o indice 7

def modalidades(bd):
    lista = []
    for elem in bd:
        if elem[7] not in lista:
            lista.append(str(elem[7]))
    lista.sort()
    return lista


def distribPorModalidade(bd):
    distribuicaoMod = {}
    for elem in bd:
        if elem[7] in distribuicaoMod.keys():
            distribuicaoMod[elem[7]] = distribuicaoMod[elem[7]] + 1
        else:
            distribuicaoMod[elem[7]] = 1
    return distribuicaoMod


def distribPorClube(bd):
    distribuicaoClube = {}
    for elem in bd:
        if elem[8] in distribuicaoClube.keys():
            distribuicaoClube[elem[8]] = distribuicaoClube[elem[8]] + 1
        else:
            distribuicaoClube[elem[8]] = 1
    return distribuicaoClube



def distribPorAno(bd):
    distribuicaoAno = {}
    for elem in bd:
        data = elem[1]
        ano = data[:4]
        if ano in distribuicaoAno.keys():
            distribuicaoAno[ano] = distribuicaoAno[ano] + 1
        else:
            distribuicaoAno[ano] = 1
    return distribuicaoAno


def distrib(bd, i):
    distr = {}
    for elem in bd:
        if i in range(0,11):
            
            if elem[i] in distr.keys():
                distr[elem[i]] = distr[elem[i]] + 1
            else:
                distr[elem[i]] = 1
        else:
            return "Campo não existente na BD!"
    return distr



# modalidade é indice 7
# distribPorModalidade(bd)

#import pandas as pd
import matplotlib.pyplot as plt


def plotDistribPorModalidade(bd):
    dic = distribPorModalidade(bd)
    x = []
    y = []
    label = []
    for e in dic.keys():
        y.append(e)
        x.append(dic[e])
    plt.barh(y,x,color = ['red', 'green', 'blue', 'yellow', 'pink'])
    plt.title('Distribuição por modalidade!') 
    plt.xlabel('Nº registos')
    plt.ylabel('Modalidade')
    plt.show()
    
BD = []
BD = lerDataset("../Algoritmos e Técnicas de Programação/emd.csv")
#lista = plotDistribPorModalidade(BD)


def plotDistrib(dist):
    dic = dist
    x = []
    y = []
    label = []
    for e in dic.keys():
        y.append(e)
        x.append(dic[e])
    plt.barh(y,x,color = ['red', 'green', 'blue', 'yellow', 'pink'])
    
    plt.title('Distribuição!') 
    plt.xlabel('Nº registos')
    plt.ylabel('Distribuição pedida')
    plt.show()
    
BD = []
BD = lerDataset("../Algoritmos e Técnicas de Programação/emd.csv")
#lista = plotDistrib(distrib(BD, 7))

'''
def plotDistribPorModalidade(bd):
    dic = distribPorModalidade(bd)
    print(dic)
    x = list(dic.keys())
    #print(x)
    y = list(dic.values())
    #print(y)
    plt.bar(x,y, width = 0.5, color = ['red', 'green', 'blue', 'yellow', 'pink'])
    plt.xlabel('Modalidade')
    plt.ylabel('Nº de EMDs')
    plt.title('Distribuição por modalidade!')   
    plt.show()
    

def plotDistrib(bd, dist):
    dic = dist
    print(dic)
    x = list(dic.keys())
    #print(x)
    y = list(dic.values())
    #print(y)
    plt.bar(x,y, width = 0.5, color = ['red', 'green', 'blue', 'yellow', 'pink'])
    plt.xlabel('Distribuição pedida')
    plt.ylabel('Nº')
    plt.title('Distribuição!')   
    plt.show()
'''


    




        