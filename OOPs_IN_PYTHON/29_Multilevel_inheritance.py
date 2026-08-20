#Multilevel Inheritance 
# Grandparent class
class Grandfather:

    def property(self):
        print("Grandfather's property")


# Parent class
class Father(Grandfather):

    def car(self):
        print("Father has a car")


# Child class
class Son(Father):

    def bike(self):
        print("Son has a bike")


# Object
s = Son()

s.property()
s.car()
s.bike()