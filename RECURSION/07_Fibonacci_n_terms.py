#Fibonacci undr n terms 

def fibonacci(n):
    #Base case 
    if n == 0:
        return 0
    if n == 1:
        return 1
    #Recursive call
    return fibonacci(n - 1) + fibonacci( n - 2)

for i in range(10):
    print(fibonacci(i))
