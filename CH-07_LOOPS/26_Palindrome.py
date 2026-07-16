#Check whether a number is Palindrome.
#Take input from users 

num = int(input("Enter Numbers: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit