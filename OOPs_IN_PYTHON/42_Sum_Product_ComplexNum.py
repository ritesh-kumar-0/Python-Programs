''' Write a class ‘Complexʼ to represent complex numbers, along with overloaded operators
‘+ʼ and ‘*ʼ which adds and multiplies them'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    #ovarloading + operator 
    def __add__(self, other):
#Add rel parts
        real_part = self.real + other.real
#Add imaginary parts
        imag_part = self.imag + other.imag
        #return new complex num
        return Complex(real_part, imag_part)

#Overloading * operator 
    def __mul__(self, other ):
         # Formula:
        # (a + bi)(c + di)
        # = (ac - bd) + (ad + bc)i
        real_part = (self.real * other.real) - (self.imag * other.imag)

        imag_part = (self.real * other.imag) + (self.imag * other.real)

        return Complex(real_part, imag_part)

    def display(self):
        print(self.real, "+", self.imag, "i")

c1 = Complex(3, 4)
c2 = Complex(4, 5)

c3 = c1 + c2
print("Addition: ")
c3.display()

c4 = c1 * c2
print("Multiplication: ")
c4.display()