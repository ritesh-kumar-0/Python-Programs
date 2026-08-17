'''Q2: . Write a class “Calculator” capable of finding square, cube and square root of a number.'''

class Calculator:
    #Constructor
    def __init__(self, n):
        self.n = n
    #Find Square 
    def square(self):
        print(f"The Square is {self.n*self.n}")
#Find Cube 
    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")
#Find Square Root
    def square_root(self):
        print(f"The Squareroot is {self.n**1/2}")

#Create Object and pass the number 
a = Calculator(5)
#Call method 
a.square()
a.cube()
a.square_root()