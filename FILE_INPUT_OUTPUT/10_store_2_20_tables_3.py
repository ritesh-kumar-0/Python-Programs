'''3. Write a program to generate multiplication tables from 2 to 20 and write it to
the different files. Place these files in a folder for a 13-year-old.'''

# Function to generate the multiplication table of a given number
def generateTable(n):

    # Store the complete table as a string
    table = ""

    # Generate the table from 1 to 10
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    # Create a file and write the table into it
    with open(f"FILE_INPUT_OUTPUT/tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 2 to 20
for i in range(2, 21):
    generateTable(i)

print("Multiplication tables from 2 to 20 have been created successfully!")
