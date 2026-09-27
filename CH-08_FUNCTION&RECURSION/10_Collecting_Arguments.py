#Collecting arguments 
# *args - allows a function to accept any number of positional arguments
#Python stores them as tuples 
def add(*args):  # *args collects all the arguments into a tuple
    sum = 0

#Loops takes each value one by one 
    for i in args:
        sum += i
    print("Total Sum = ", sum)

#Function call 
add(2, 4,5.5, 6, 8,7)