#Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter a Number: "))

#store factorial value 
fact= 1

#multiply numbers from 1 to n
for i in range(1, n + 1):

#Multiplyn current number with factorial 
    fact = fact * i
print("Factorial =", fact)
