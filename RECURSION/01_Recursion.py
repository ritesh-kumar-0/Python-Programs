#Printing Numbers 1 to 5

def print_num(n):

    # Base Case
    if n == 6:
        return

    # Print current number
    print(n)

    # Recursive Call
    print_num(n+1)

print_num(1)