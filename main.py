#Abstract
from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is moving!")

class Boat(Vehicle):
    def go(self):
        print("The boat is moving!")



boat = Boat()
car = Car()

boat.go()
car.go()