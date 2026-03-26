'''Write a program to find the greatest of four numbers entered by the user.'''
a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))
c = int(input("Enter num 3: "))
d = int(input("Enter num 4: "))

if (a>b and a>c and a>d):
    print("Greatest number is a : ", a)
elif(b>a and b>c and b>d):
    print("Greatest number is b: ", b)
elif(c>a and c>b and c>d):
    print("Greatest number is c: ", c)
else:
    print("Greatest number is d: ", d)