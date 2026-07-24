#Function with parameters
#function to add two numbers
def add_num(num1 , num2):  # nnum1 and num2 is parameters
    return num1 + num2
#Taking user input
a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
#Function call 
result = add_num(a , b)
print("Sum =", result)
