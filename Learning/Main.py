class Main:
    pass

from Cliente import Cliente
from Conta import Conta


#instancia do objeto
c1 = Cliente("João" , "12996364525")


conta=Conta(123, c1.get_nome())

conta.depositar(100)
conta.saque(30)
conta.extrato()

print(conta._titular, conta._numero, conta._saldo)