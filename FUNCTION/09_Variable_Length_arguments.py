#Variable Length Arguments 
'''*args allows a function to accept any number of positional arguments.
Python stores them as a tuple.'''

# Function to add any number of numbers
def add(*numbers):

    total = 0

    # Loop through all numbers
    for i in numbers:
        total += i

    print("Total =", total)

add(10, 20, 30, 40, 50)