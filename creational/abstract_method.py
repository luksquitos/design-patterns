#TODO Colocar explicação sobre abstract_method

from abc import ABC, abstractmethod, abstractstaticmethod

# Carro Luxo

class CarroLuxo(ABC):
    
    @abstractmethod
    def buscar_cliente(self): pass
    
    
class CarroLuxoPrincipal(CarroLuxo):

    def buscar_cliente(self):
        print("Carro de luxo da empresa principal está buscando cliente")


class CarroLuxoFilial(CarroLuxo):
    
    def buscar_cliente(self):
        print("Carro de luxo da empresa filial está buscando cliente")


# Carro popular

class CarroPopular(ABC):
    
    @abstractmethod
    def buscar_cliente(self): pass


class CarroPopularPrincipal(CarroPopular):
    
    def buscar_cliente(self):
        print("Carro popular da empresa principal está buscando cliente.")


class CarroPopularFilial(CarroPopular):
    
    def buscar_cliente(self):
        print("Carro popular da empresa filial está buscando cliente")


# Factories

class BuscarCarro(ABC):
    
    @abstractstaticmethod
    def buscar_carro_luxo(self) -> CarroLuxo: ...
    
    @abstractstaticmethod
    def buscar_carro_popular(self) -> CarroPopular:...
 

class BuscarCarroPrincipal(BuscarCarro):
    
    @staticmethod
    def buscar_carro_luxo() -> CarroLuxo:
        print("Cliente pediu carro de luxo da empresa principal")
        return CarroPopularPrincipal()

    @staticmethod
    def buscar_carro_popular() -> CarroPopular:
        print("Cliente pediu carro popular da empresa principal")
        return CarroPopularPrincipal()


class BuscarCarroFilial(BuscarCarro):
    
    @staticmethod
    def buscar_carro_luxo() -> CarroLuxo:
        print("Cliente pediu carro de luxo da empresa filial")
        return CarroPopularFilial()

    @staticmethod
    def buscar_carro_popular(self) -> CarroPopular:
        print("Cliente pediu carro popular da empresa filial")
        return CarroPopularFilial()
    
    
if __name__ == "__main__":
    cliente_1 = BuscarCarroFilial.buscar_carro_luxo()
    cliente_2 = BuscarCarroPrincipal.buscar_carro_luxo()
