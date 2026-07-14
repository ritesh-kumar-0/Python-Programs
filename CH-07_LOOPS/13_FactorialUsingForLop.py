#Factorial Using For loop

num = 5
fact = 1 # Factorial starts with 1

# Loop from 1 to n
for i in range(1,num+1):
 # Multiply current value
    fact = fact * i
# Print factorial
print(fact)