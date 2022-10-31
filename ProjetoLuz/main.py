
from classes import Consumidor, Objeto
from util import criaObjeto, listarObj



nomeConsumidor = input('Digite seu nome: ')
consumidor = Consumidor(nomeConsumidor)

menu = -1
while menu != 0:
    menu = int(input('\n\n[1] - Adicionar objeto\n[2] - Alterar região\n[3] - Calcular consumo\n[4] - Visualizar objetos\n[0] - Sair\nEscolha uma opção: '))
    if menu == 1:
        novoObj = criaObjeto()
        #print('novo obj:', novoObj.nome)
        consumidor.addObjeto(novoObj)

    elif menu == 4:
        listarObj(consumidor)


# prints auxiliares (debug)
print('nome do consumidor:', consumidor.nome)
print('objetos do consumidor: ', consumidor.objetos[0].nome)
