# TPC2

**Título:** TPC2                                                       
**Autor:**  Ricardo Lopes Barros, A96730;                             
**Data de início:** 2021-10-11;   
**Data de fim:** 2021-10-16;   
**Supervisor:** José Carlos Ramalho, https://www.di.uminho.pt/~jcr/

----



Para criar o algoritmo que faz com que o computador adivinhe o número que o jogador escolheu ( _n_ ), entre 0 e 100, foi utilizada a pesquisa binária, pelo que o número máximo de tentativas, neste caso, seria 7.

Depois de definir a função da procura ( _pb()_ ), fez-se um _input_ para que o utilizador escolha um número entre 0 e 100 e a verificação de que esse intervalo foi cumprido.

Caso seja cumprido o intervalo, prossegue. Foi definido um limite inferior( _0_ ) e um limite superior( _100_ ) (os valores limite do intervalo) e foi definida a variável _tpc_ , que é a tentativa de adivinhar do computador e é igual à divisão inteira da soma do limite inferior com o superior por 2 ( _(li + ls) // 2_ ).

Foi criado um ciclo em que enquanto a tentativa do computador for diferente do número escolhido pelo utilizador, o computador utilizará outra vez a mesma equação para escolher um número, mas haverão ajustes.

Se o nº que adivinhou for menor do que o nº do utilizador, o limite inferior passará a ser o nº que adivinhou mais 1 (de modo a não o incluir no novo intervalo de possíveis escolhas).

Se o nº que adivinhou for maior do que o nº do utilizador, o limite superior passará a ser o nº que adivinhou.

Assim que a tentativa do computador esteja correta ( _tpc == n_ ), é dado como terminada a pesquisa, sendo imprimida a mensagem de vitória do computador.
