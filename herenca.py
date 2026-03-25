
#TODO Criação de uma class Admin (adm) para a class Usuário (user)

class User:
    def __init__(self):
        self.__nameUser = "William"

    def setName(self, name):
        if name.strip() != "":
            self.__nameUser = name

    def getName(self):
        return self.__nameUser

class Adm(User):
    def name(self):
        print(self.getName())

    def escreverNome(self):
        return "Admin"

    def digaOla(self):
        return "Olá consultor, " + adm.getName()




adm = Adm()
adm.setName("Patrick Jane")

adm.name()
print(adm.escreverNome())
print(adm.digaOla())