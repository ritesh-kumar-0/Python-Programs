'''. Override the __len__() method on vector of problem 5 to display
 the dimension of the vector.'''
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Display vector in i, j, k format
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    # Return the dimension of the vector
    def __len__(self):
        return 3


# Create a vector
v = Vector(7, 8, 10)

print(v)
print("The dimension of the vector: ", len(v))