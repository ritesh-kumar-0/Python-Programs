#Print numbers 5 to 1

def reverse(n):
    #Base case 
    if n == 0:
        return
    #print current value 
    print(n)

    #Recursive call
    reverse(n-1)
reverse(5)