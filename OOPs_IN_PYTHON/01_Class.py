#Class

class Employee:
    language ="Python" #This is class attribute 
    salary = 1200000

ritesh = Employee()
ritesh.name = "Ritesh" #This is an instance attribute 
print(ritesh.name, ritesh.language,ritesh.salary)

rohan = Employee()
rohan.name = "Rohan Roy"
print(rohan.name, rohan.language,rohan.salary)

'''here name is object attribute and salary and language are class attributes
 as they directly belong to the class'''
