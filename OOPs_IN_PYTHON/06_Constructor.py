class Employe:
    language = "Python" #class attribute
    salary = 120000

    def __init__(self, name , salary, language): # dunder method which is automatically called 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self): 
# Display employee information
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod #means this method doesn't need self.
    def greet():
        print("Good Morning")

# Creating an object
ritesh = Employe("Ritesh", 130000, "JavaScript")
# Calling getInfo() method
ritesh.getInfo()
# Printing object attributes
print(ritesh.name, ritesh.salary, ritesh.language )