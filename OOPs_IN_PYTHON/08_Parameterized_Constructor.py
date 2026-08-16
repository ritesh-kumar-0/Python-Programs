#Parameterized Constructor

class Student:

#Parameterized Constructor
    def __init__(self, name , age, course):
# Store parameter values in object attributes
        self.name = name
        self.age = age
        self.course = course 

# Creating objects with different data
s1 = Student("Ritesh", 20, "BTech CSE")
s2 = Student("Raj", 21, "BCA")

#Dispaly Student 1
print(s1.name)
print(s1.age)
print(s1.course)

print()

#Student 2
print(s2.name)
print(s2.age)
print(s2.course)