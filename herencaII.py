
#TODO 01
class Pessoa:
    def __init__(self):
        self.nomePessoa = ""
        self.idadePessoa = ""

    def setNome(self, nome):
        if nome.strip() != "":
            self.nomePessoa = nome

    def getNome(self):
        return self.nomePessoa

    def setIdade(self, idade):
        if idade >= 0:
            self.idadePessoa = idade

    def getIdade(self):
        return self.idadePessoa

class Aluno(Pessoa):
    def nome(self):
        print(self.getNome)

    def idade(self):
        print(self.getIdade)

    def nota(self):
        nota = 10