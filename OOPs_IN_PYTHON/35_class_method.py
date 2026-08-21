class Student:

    university = "Shoolini University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_university(cls, name):
        cls.university = name


s1 = Student("Ritesh")
s2 = Student("Rahul")

print(s1.university)
print(s2.university)

Student.change_university("NIT kanpur")

print(s1.university)
print(s2.university)