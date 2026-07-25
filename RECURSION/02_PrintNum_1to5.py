#Printing Numbers 1 to 5

def print_num(n):
    #Base case 
    if n == 6:
        return
    #print current number
    print(n)

    #Recursive Call
    print_num(n+1)

print_num(1)
