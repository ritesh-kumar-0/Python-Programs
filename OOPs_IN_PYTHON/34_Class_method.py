#Class Method 
#@classmethod decorator is used to create a class method 

class Student:

    school = "Shoolini University"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


# Accessing classmethod using class
print(Student.school)

Student.change_school("IIT Delhi")

print(Student.school)