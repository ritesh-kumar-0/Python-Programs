'''Q:1. Create a class “Programmer” for storing information of few programmers working at
Microsoft.'''

class Programmer:

    company = "Microsoft"
    def __init__(self , name , language , salary):
        self.name = name 
        self.language = language 
        self.salary = salary

#Dispaly Information 
print("Programmer 1:")
p1 = Programmer("Ritesh", "Python", 1200000)
print(p1.name, p1.language, p1.salary )

print()

print("Programmer 2:")
p2 = Programmer("Kundan", "C++", 1100000)
print(p2.name, p2.language, p2.salary )



