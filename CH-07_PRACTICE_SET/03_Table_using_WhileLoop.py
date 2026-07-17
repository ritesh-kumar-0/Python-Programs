#Write a program to print multiplication table of a given number using While loop
#Taking user input 

num = int(input("Enter the Number: "))
i = 1
while i <=10:
    print(num, "*", i, "=", num * i)
    i += 1