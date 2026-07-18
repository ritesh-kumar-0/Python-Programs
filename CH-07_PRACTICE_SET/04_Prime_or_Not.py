#Write a program to find whether a given number is prime or not.

num = int(input("Enter the Numbers: "))

if num <= 1:
    print(num, "is not a Prime Number")

else:
# Check for factors from 2 up to the square root of the number
# num ** 0.5 = Square Root of num
# int() converts the square root to an integer
# +1 is used because the last value in range() is not included
 for i in range(2, int(num ** 0.5) + 1):

 # Check if 'i' is a factor of num
# If remainder is 0, then 'i' divides num completely
    if num % i == 0:
        print("Not a Prime Number")
        break
 else:
    print(num, "is a prime Number")

#We check only up to the square root of the number because if a number has a factor 
# greater than its square root, it must also have a corresponding factor smaller than its square root.
#This makes the program much faster than checking all numbers up to num - 1.