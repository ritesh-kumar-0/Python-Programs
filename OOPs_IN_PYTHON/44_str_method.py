''' Write __str__() method to print the vector as follows:
7i + 8j + 10k    Assume vector of dimension 3 for this problem.'''

class Vector:
# Initialize the vector with x, y, and z components
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
# Return the vector in i, j, k format
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

# Create a vector object
v = Vector(7, 8, 10)

print(v)