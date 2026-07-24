#Default Arguments
'''A Default Argument is a parameter that already has a default value.
If the user does not provide a value, Python uses the default value'''
# Function with default country
def student(name, country="India"):
    print("Name:", name)
    print("Country:", country)

#taking user input 
name = input("Enter your name:")

student(name)