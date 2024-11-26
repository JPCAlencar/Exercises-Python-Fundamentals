from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")
    
    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self):
        return "Samsung"

class ControleAr(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "Comfee"



controle =  ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle =  ControleAr()
controle.ligar()
controle.desligar()
print(controle.marca)