class Cliente:
    def __init__(self, n, fone ):
        self._nome = n 
        self._telefone = fone 

        #pass <--quando nehuma estrutura será deifinida

    #Métodos de acesso
    def get_nome(self):
        return self._nome
    
    
    def set_nome(self, nome):
        self.nome = nome


