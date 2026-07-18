#Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter Number:"))

sum = 0
i = 1

while i <= n:
 # Add the current value of i to sum
    sum += i
# Increase i by 1
    i += 1

print("Sum is: ", sum)