class Pessoa:

    # Metodo construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print('Ola seja bem vinda: ', self.Nome)

    def Recusado(self):
        print('Seu acesso foi recusado')

    # Funcao
    def Maior_Idade(self):
        if self.Idade >= 18:
            print('O usuario é maior de idade')
            self.Boas_Vindas()
        else:
            print('O usuario é menor de idade')
            self.Recusado()


Dados = Pessoa('Camille', 20)
Dados.Maior_Idade()
