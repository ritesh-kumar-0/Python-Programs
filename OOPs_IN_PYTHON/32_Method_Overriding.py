#Method Overriding
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    # Overriding parent's method
    def sound(self):
        print("Dog says Woof")


dog = Dog()

dog.sound()