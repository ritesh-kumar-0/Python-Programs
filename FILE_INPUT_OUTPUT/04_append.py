# Append mode (a)
'''Adds new data at the end of the file.
Old data remains safe.'''
str = "Hey ritesh  !"

f = open("file.txt", "a")
f.write("\nWelcome")

f.close()