class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False

    def wake_up(self):
        if not self.asleep:
            raise RuntimeError
        self.asleep = False
    def sleep(self):
        if self.asleep:
            raise RuntimeError
        self.asleep = True
    def __str__(self) -> str:
        return self.name
    
class Lion(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
    
    def roar(self):
        print("ROARRR!!!")


class Owl(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.diurnal = False
        self.nb_legs = 2
    
    def fly(self):
        pass

class Giraffe(Animal):
    def __init__(self, name: str, neck_length) -> None:
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
        if not ((type(neck_length) == int or type(neck_length) == float) and neck_length >= 0):
            raise ValueError
        self.neck_length = neck_length
            
        
    
    def fly(self):
        pass

class Zoo:
    def __init__(self) -> None:
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise ValueError
        self.animals.append(animal)
    def __str__(self) -> str:
        s = f"Le zoo est constitué de {len(self.animals)}\n"
        for animal in self.animals:
            s += str(animal) + "\n"
        return s
def create_my_zoo()-> Zoo:
    zoo = Zoo()
    zoo.add_animal(Lion("Simba"))
    zoo.add_animal(Giraffe("BigNeck", 1100))
    zoo.add_animal(Owl("hiboucoubeh"))
    zoo.add_animal(Owl("hiboucoubeh 2"))
    return zoo

