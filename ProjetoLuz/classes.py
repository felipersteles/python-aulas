
class Consumidor:

    def __init__(self, nome):
        self.nome = nome
        self.objetos = []

    def addObjeto(self, objeto):
        self.objetos.append(objeto)
    
    def getObjetos(self):
        return self.objetos

class Objeto:
    def __init__(self, nome, uso, consumo):
        self.nome = nome
        self.uso = uso
        self.consumo = consumo

    
        
