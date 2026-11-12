class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Wanwan")
class Cat(Animal):
    def make_sound(self):
        print("Nya-")
class Cow(Animal):
    def make_sound(self):
        print("Mo-")
animals = [Dog(), Cat(), Cow()]
for box in animals:
    box.make_sound()
dog = Dog()
dog.make_sound()
