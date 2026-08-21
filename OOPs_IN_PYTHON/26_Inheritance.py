#INHERITANCE 
# Parent class
class Animal:

    def eat(self):  
        print("Animal is eating")


# Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


# Creating object 
dog = Dog()

# Method inherited from Animal
dog.eat()

# Method of Dog
dog.bark()