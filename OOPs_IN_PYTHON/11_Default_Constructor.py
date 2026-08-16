#Default Constructor 
class Car:
    #Constructor without parameter 
    def __init__(self):

        #initialize default values 
        self.brand = "Toyota"
        self.color = "Black"

    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

#creating an object 
c1 = Car()
#Calling the method 
c1.display()

