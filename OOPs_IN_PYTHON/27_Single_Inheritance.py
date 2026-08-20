#Single Inheritance 
# Parent class
class Father:

    def house(self):
        print("Father house")


# Child class
class Son(Father):

    def bike(self):
        print("Son  bike")


# Object
s = Son()

s.house()  # Inherited method
s.bike()   # Child's own method