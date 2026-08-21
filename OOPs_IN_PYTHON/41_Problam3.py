'''Q: 3. Create a class ‘Employeeʼ and add salary and increment properties to it.
 Write a method ‘salaryAfterIncrementʼ method with a @property decorator with a 
 setter which changes the value of increment based on the salary'''
class Employee:

    def __init__(self, salary, increment_percent):
        self.salary = salary
        self.increment_percent = increment_percent

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment_percent / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment_percent = (
            (new_salary - self.salary) / self.salary
        ) * 100


# 50000 salary with 10% increment
e = Employee(50000, 10)

print("Salary:", e.salary)
print("Increment:", e.increment_percent, "%")
print("Salary after increment:", e.salaryAfterIncrement)

# Change final salary
e.salaryAfterIncrement = 60000

print("New Increment:", e.increment_percent, "%")