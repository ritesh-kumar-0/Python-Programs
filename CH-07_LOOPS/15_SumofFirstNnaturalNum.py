#WAP to calculate the sum of first N Natural Number
#taking user input 
n = int(input("Enter the Number: "))
#Variable to store sum 
sum = 0
#Loop 
for i in range(1,n+1):
    sum = sum + i
print (sum)