#Parameterized Constructor 

class Car:

    def __init__(self, brand, color):

        self.brand = brand
        self.color = color

#Creating object with different values 
c1 = Car("BMW", "Black")
c2 = Car("Audi", "White")

#dispaly information 
print(c1.brand, c1.color)
print(c2.brand, c2.color)