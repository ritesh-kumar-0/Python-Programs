#Factorial using Recursion 

def factorial(n):
    if n == 1 or n == 0: #Base case 
        return 1
    #recursive Case 
    return n * factorial(n-1)
n = int(input("Enter Number: "))


print("The factorial of given number is: ", factorial(n))

    
    