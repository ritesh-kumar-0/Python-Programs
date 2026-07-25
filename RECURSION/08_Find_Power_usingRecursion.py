#Find power using Recursion 
'''The power of a number means multiplying a number by itself a certain
 number of times.
 We know that:
power(a, b) = a x power(a, b-1)
'''
# Function to calculate power using recursion
def power(base , exponent):

    #Base case 
    if exponent == 0:
        return 1
    #Recursive Case
 # Multiply the base with the result of power(base, exponent - 1) 
    return base * power(base , exponent - 1)

#Take base value 
base = int(input("Enter the base number: "))
#Take exponent 
exponent = int(input("Enter the exponent: "))

#Call the recursive funtion and store result 
result = power(base, exponent)

print("Answer =", result)

