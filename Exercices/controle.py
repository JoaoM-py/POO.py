class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_canais = []
        self.volume = 20
    
    def aumentarVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100
    

    def diminuirVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocarCanal(self, canal):
        if canal in self.lista_canais:
            self.canal_atual = canal


    def adicionarCanal(self, canal):
        if canal not in self.lista_canais:
            self.lista_canais.append(canal)   
        


class ControleRemoto:
    def __init__(self,tv):
        self.tv = tv


    def aumentaVolume(self):
        self.tv.aumentarVolume(90)

    def diminuiVolume(self):
        self.tv.diminuirVolume(90)

    def trocaCanal(self, canal):
        self.tv.trocarCanal(canal)
    
    def adicionaCanal(self, canal):
        self.tv.adicionarCanal(canal)

    