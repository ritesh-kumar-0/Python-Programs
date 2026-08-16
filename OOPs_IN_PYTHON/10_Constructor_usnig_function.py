
class Student:
    def __init__(self, name, marks):
        #initialize attributes
        self.name = name
        self.marks = marks

    #normal method
    def display(self):
        print("Student Name:", self.name)
        print("marks:", self.marks)

#creating an object 
s1 = Student("Ritesh", 85)

#callinng the normal method 
s1.display()