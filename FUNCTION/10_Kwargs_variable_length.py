'''**kwargs allows a function to accept any number of keyword arguments.
Python stores them as a dictionary.'''

# Function to display student details
def student(**data):

    # Loop through dictionary
    for key, value in data.items():
        print(key, ":", value)

student(name="Ritesh", age=20, city="Patna")