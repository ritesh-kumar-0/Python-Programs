#Hierarchical Inheritance
'''When multiple child classes inherit from one parent class'''
# Parent class
class Animal:

    def eat(self):
        print("Animal is eating")


# Child class 1
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


# Child class 2
class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


# Objects
dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()  