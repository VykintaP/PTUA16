from abc import ABC, abstractmethod


# Abstrakti klasė
class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


# Konkretizuota klasė Dog
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Bark!")


# Konkretizuota klasė Cat
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")


# Konkretizuota klasė Fox
class Fox(Animal):
    def make_sound(self):
        print(f"{self.name} says: What does the fox say?")


# Gyvūnų sąrašas
animals = [
    Dog("Pupper"),
    Cat("Kitty"),
    Fox("Foxy"),
    Dog("Barky"),
]

# Implementacija be abstrakčios klasės (naudojant isinstance)
print("Using isinstance checks:")
for animal in animals:
    if isinstance(animal, Dog):
        print(f"{animal.name} says: Bark!")
    elif isinstance(animal, Cat):
        print(f"{animal.name} says: Meow!")
    elif isinstance(animal, Fox):
        print(f"{animal.name} says: What does the fox say?")

# Implementacija naudojant abstrakčią klasę
print("\nUsing abstract class and make_sound method:")
for animal in animals:
    animal.make_sound()
