class Prey:
    def flee(self):
        print("This animal is fleeing!")
class Predator:
    def hunt(self):
        print("This animal is hunting!")

class Rabbit:
    def flee(self):
        print("this rabbit is fleeing")

class Tiger:
    def hunt(self):
        print("This tiger is hunting")

class Fish:
    def hunt(self):
        print("The big fish is hunting")
        return self
    def flee(self):
        print("The small fish is fleeing")
        return self
fish = Fish()
rabbit = Rabbit()
tiger = Tiger()
prey = Prey()
predator = Predator()

fish.hunt().flee()
tiger.hunt()
rabbit.flee()
prey.flee()
predator.hunt()