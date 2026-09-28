#Write a function largest_number() that accepts any number of numbers and finds the largest number.
# largest_number(10, 45, 23, 89, 12)  , Expected output : 89

def largest_number(*num):
    #Assume the first number is the largest initially
    largest = num[0]

    #Check every number
    for n in num:
        if n > largest:
            largest = n
    return largest # resturn largest Number 

#calling the function

result = largest_number(10, 45, 23, 89, 12)

print(result)
