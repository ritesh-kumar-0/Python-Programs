'''One of the biggest advantages of constructors is that we can
 create multiple objects with different data.'''
class Employee:

    #constructor 
    def __init__(self, name, salary):
# Initialize employee information
        self.name = name
        self.salary = salary

#Creating different Employee objects
e1 = Employee("Ritesh", 50000)
e2 = Employee("Aman", 60000)
e3 = Employee("Rahul", 45000)
#Display employee information 

print(e1.name, e1.salary)
print(e2.name, e2.salary)
print(e3.name, e3.salary)
        