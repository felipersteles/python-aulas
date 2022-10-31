kwh = 0 

# armazenando os objetos em um array e o consumo deles em uma estrutura chamada dicionario(procura no google)
objetos=['GELADEIRA','FORNO ELETRICO','AIR FRYER','TELEVISÃO','VENTILADOR','AR-CONDICIONADO','CHUVEIRO ELETRICO','FREEZER','COMPUTADOR','LAMPADA','CARREGADOR']
consumoObjetos = {
    'GELADEIRA': 35,
    'FORNO ELETRICO': 5,
    'AIR FRYER': 2,
    'TELEVISÃO': 7,
    'VENTILADOR': 7,
    'AR-CONDICIONADO': 20,
    'CHUVEIRO ELETRICO': 15,
    'FREEZER': 2,
    'COMPUTADOR': 20,
    'LAMPADA': 3,
    'CARREGADOR': 5
}

op = -1
while op!=0:
  print('''
  [1] - NORTE 
  [2] - NORDESTE
  [3] - CETRO-OESTE
  [4] - SUDESTE
  [5] - SUL
  [0] - SAIR
  ''') 
  
  op=int(input('QUAL REGIÃO VOCÊ MORA ?\nResposta: '))
  
  if op==1:
    kwh=167.6
    break
    
  elif op==2:
    kwh=125.2
    break
  elif op==3:
    kwh=187.4
    break
  elif op==4:
    kwh=172.9
    break 
  elif op==5:
    kwh=181.6
    break
  else:
    print('Opção inválida. Tente novamente.')

print(kwh)    
print("\n=========================================================================================\n")
for i in range(len(objetos)):
    print(i,": ",objetos[i])
  
resp=int(input('\nAdicone os eletrodomesticos da lista: '))
objeto=objetos[resp]
horas = int(input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))

formulaConsumo = ((consumoObjetos[objeto] * 0.003) * horas)
formulaValor = formulaConsumo * kwh

print(f'A(o) {objeto.lower()} consumiu {formulaConsumo} kw e custou um total de {formulaValor} reais')