class Conta:
    def __init__(self, numero, titular):
        self._saldo = 0.0
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo 


    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo
    
    def saque(self, valor):
        if(self.saldo>= valor):
            self.saldo -= valor
        else:
            print("saldo insuficente")     
    
    def depositar(self, valor):
        self.saldo += valor
    
    def extrato(self):
        print("Cliente", self._titular, "Saldo atual", self._saldo)

# def get_saldo(self):
#     return self.saldo


# def set_saldo(self, saldo):
#     if(saldo < 0):
#         print("Saldo não pode ser negativo")
#     else:
#         self._saldo = saldo 



    