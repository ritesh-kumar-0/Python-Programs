#Conswtructor With Calculation 

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        #Store student name
        self.name = name

#Store marks 
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

#calculate total marks
        self.total = marks1 + marks2 + marks3
#Calculate average
        self.average = self.total / 3

#Creating an object 
s1 = Student("Ritesh", 80, 85, 90)

# Display results
print("Name:", s1.name)
print("Total:", s1.total)
print("Average:", s1.average)
