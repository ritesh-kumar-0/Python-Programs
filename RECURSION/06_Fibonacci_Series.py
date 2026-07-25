#Fibonacci Series 
#Every number is the sum of the previous two numbers

def fibonacci(n):
    #base case 
    if n == 0:
        return 0
    if n == 1:
        return 1

    #Recursive case 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#taking user input 
terms = int(input("Enter The Number of terms: "))
print("Fibonacci Series: ")
#Loop from 0 to term -1 

for i in range(terms):
    print(fibonacci(i), end=" ")# end=" " prints all numbers on the same line
