#TODO Descrição do padrão factory method.

class Animal:
    def som(self):
        raise NotImplemented("Implemente o método 'som'")


class Cachorro(Animal):
    def som(self):
        print('AUAU')

    
class Gato(Animal):
    def som(self):
        print("MIAU")


def AnimalFactory(animal: str = None, random=False):
    animais = {
        "cachorro": Cachorro(),
        "gato": Gato()
    }
    
    if random and animal is None:
        from random import choice
        animal = choice(
            list(animais.keys())
        )
    
    assert animal in animais.keys(), (
        "Animal '%s' não encontrado" %
        animal
    )
    
    return animais.get(animal)


if __name__ == "__main__":
    animal_1 = AnimalFactory("cachorro")
    animal_2 = AnimalFactory(random=True)
    animal_3 = AnimalFactory('girafa')
