#WAP to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))

# Loop from 10 down to 1
for i in range(10,0, -1):
    print(f"{n} x {i} = {n * i}")