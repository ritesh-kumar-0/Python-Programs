# Sum of N numbers 

def sum(n):
    #base case 
    if n == 0:
        return 0

    #recursive case 
    return n + sum(n-1)
n = int(input("Enter Numbers: "))
print("Sum of ",n,"numbers is ",sum(n))