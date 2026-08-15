
class Employe:
    language = "Python" #class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

ritesh = Employe()
#ritesh.language = "JavaScript" #An instance attribute

ritesh.getInfo()