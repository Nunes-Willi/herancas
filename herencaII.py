
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
        #TODO 02
class Veiculo:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0

    def setMarca(self, marca):
        if marca.strip() != "":
            self.marca = marca

    def getMarca(self):
        return self.marca

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.portas = 0

    def info(self):
        print(self.getMarca(), self.modelo, self.portas)

class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.cilindradas = 0

    def info(self):
        print(self.getMarca(), self.modelo, self.cilindradas)


#TODO 03
class Animal:
    def __init__(self):
        self.nome = ""
        self.peso = 0

    def comer(self):
        print("Comendo...")

class Cachorro(Animal):
    def latir(self):
        print("Au au!")

class Gato(Animal):
    def miar(self):
        print("Miau!")


#TODO 04
class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self.salario = 0

    def aumento(self, percentual):
        self.salario += self.salario * (percentual / 100)


#TODO 05
class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self):
        self.comprimento = 0
        self.largura = 0

    def area(self):
        return self.comprimento * self.largura

class Circulo(Forma):
    def __init__(self):
        self.raio = 0

    def area(self):
        return 3.14 * (self.raio ** 2)


#TODO 08
class Ingresso:
    def __init__(self):
        self.valor = 0

    def imprimeValor(self):
        print(self.valor)

class VIP(Ingresso):
    def __init__(self):
        super().__init__()
        self.adicional = 0

    def valorVIP(self):
        return self.valor + self.adicional

class Normal(Ingresso):
    def tipo(self):
        print("Ingresso Normal")

class CamaroteInferior(VIP):
    def __init__(self):
        super().__init__()
        self.localizacao = ""

    def imprimeLocalizacao(self):
        print(self.localizacao)

class CamaroteSuperior(VIP):
    def valorSuperior(self):
        return self.valorVIP()