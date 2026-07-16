#Find the sum from 1 to N.

num = int(input("Enter Number: "))
sum = 0
i = 1 

while i <= num:
    print(i)  #Print current Number

    sum = sum + i  #Add current number to sum 
    i = i + 1  #Move to next number 
print("Sum = ", sum)