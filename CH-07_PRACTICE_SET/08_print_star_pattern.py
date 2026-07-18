'''Write a program to print the following star pattern.
  *
 ***
***** for n = 3'''
n = int(input("Enter Number of rows : "))

#Outer loop for rows 
for i in range(1, n + 1):
#Print spaces 
    print(" " * (n - i), end="")
#print stars 
    print("*" * (2 * i - 1 ))
