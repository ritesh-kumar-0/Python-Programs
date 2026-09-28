# Write a function calculate_sum() that accepts any number of numbers and returns their sum.
# Calculate_sum(10, 20, 30, 40) 

# *num collects all arguments into a tuple 
def calculate_sum(*num):
    total = 0  

    for n in num:   #Loop through each number 
        total += n
    return total

#call the Function 
result = calculate_sum(10, 20, 30, 40)
print(result)    #Output: 100