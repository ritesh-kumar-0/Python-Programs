#WAP to fill in a letter template 
# Take user input
name = input("Enter your name: ")
date = input("Enter date: ")

# Letter template
letter = f"""
Dear {name},

You are selected!

Date: {date}
"""

# Print the letter
print(letter)