#Constructor With attribute 
class Student:
    #constructor 
    def __init__(self):
        #initializing object attributes
        self.name = "Ritesh"
        self.age = 20
        self.course = "CSE"

#Creating an object 
student1 = Student()
#Accessing object 
print(student1.name)
print(student1.age)
print(student1.course)

