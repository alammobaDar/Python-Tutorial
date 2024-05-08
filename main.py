#Duct typing
#Object Parameter

class Tiger:
    def roar(self):
        print("The Tiger roared!")

    def hunt(self):
        print("The tiger is hunting!!")
class Lion:
    def roar(self):
        print("The Lion roared!")

    def hunt(self):
        print("The lion is hunting!!")

class Person():
    def saw(self,tiger):
        tiger.roar()
        tiger.hunt()
        print("You saw a wild creature!!!")

tiger = Tiger()
lion = Lion()
person = Person()


person.saw(lion)