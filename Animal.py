

class Animal:
    # def __init__(self, Name, Species, Color, Size):
    #     self.Name = Name
    #     self.Species = Species
    #     self.Color = Color
    #     self.Size = Size

    def eat(self):
        print(self.Name + " the " + self.Species + " is eating ")

    def sleep(self):
        print(self.Name + " the " + self.Species + " is Sleeping ")
class Mammal(Animal):
    def reproduction(self):
        print("Mammals don't lay eggs!")
class Dog(Mammal):
    def bark(self):
        print("The Dog is barking!")

dog = Dog()
dog.bark()
dog.reproduction()
