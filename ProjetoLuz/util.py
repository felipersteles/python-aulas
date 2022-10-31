
from classes import Consumidor, Objeto

def criaObjeto():
    nomeObjeto = input('\n\nNome do objeto: ')
    tempo = input('Tempo de consumo medio diario: ')
    potencia = input('kwh: ')

    return Objeto(nomeObjeto, tempo, potencia)


def listarObj(consumidor):
    print(f'\n\nLista de objetos do consumidor {consumidor.nome}')
    for i in range(len(consumidor.objetos)):
        print(f'{i}: {consumidor.objetos[i].nome} é utilizado {consumidor.objetos[i].uso} horas por dia com o custo de {consumidor.objetos[i].consumo} kwh mensal')

