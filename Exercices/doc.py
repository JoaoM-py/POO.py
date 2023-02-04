import math



class pessoa:
    "Esta é uma classe"
    idade = 15
    def saudaçao(self):
        print("Olá pessoas")



# print(pessoa.__doc__)#docstring
# print(pessoa.idade)
# print(pessoa.saudaçao)

# Jonas = pessoa()
# print(Jonas.saudaçao)#objeto
# Jonas.saudaçao()#método 


class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol =  (4/3)*math.pi*(self.raio**3)
        return vol
    
    def area(self):
        ar= 4*math.pi*(self.raio**2)
        return ar


esfera1 =  Esfera('Azul', 4)
esfera2 =  Esfera('Preto', 8)


print(f'Volume bola1:{esfera1.volume()}')
print(f'Area bola2:{esfera2.area()}')


print(esfera1.volume())
print(Esfera.volume(esfera1))




        