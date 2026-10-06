# Tye hint in classes 
class Student:
    name:str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

student = Student("Ritesh", 20)

print(student.name)
print(student.age)