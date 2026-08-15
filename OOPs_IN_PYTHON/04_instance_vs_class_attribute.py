#Instance vs class attribute 
class Employe:
    language = "Python" #class attribute
    salary = 120000

ritesh = Employe()
ritesh.language = "JavaScript" #An instance attribute
print(ritesh.language, ritesh.salary)
