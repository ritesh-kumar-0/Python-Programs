class Student:

    def __init__(self, name, age):
        # Public attributes
        self.name = name
        self.age = age


student = Student("Ritesh", 20)

# Accessing public attributes
print(student.name)
print(student.age)