from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    # Abstract method
    @abstractmethod
    def sound(self):
        pass


# Child class
class Dog(Animal):

    # Implementing abstract method
    def sound(self):
        print("Dog says: Woof")


# Child class
class Cat(Animal):

    # Implementing abstract method
    def sound(self):
        print("Cat says: Meow")


# Creating objects
dog = Dog()
cat = Cat()

# Calling methods
dog.sound()
cat.sound()