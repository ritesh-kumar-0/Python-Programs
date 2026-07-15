#Print the multiplication table of a number.
num = int(input("Enter Number: "))
# Start the counter from 1
i = 1

# Run the loop until 10
while i <= 10:
    print(num, "*", i, "=", num * i) #Print Table 
    i = i+1 #increase i by 1
