#Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    #base case 
    if (n == 1):
        return 1
#Recursive case 
    result = sum(n - 1) + n
    return result
n = int(input("Enter Number:"))
#Call the function and store the return valued 
result = sum(n)

print("Sum of ", n , "number is = ", result )