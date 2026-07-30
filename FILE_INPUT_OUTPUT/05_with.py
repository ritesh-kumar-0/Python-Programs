
#Open the file 
f = open("FILE_INPUT_OUTPUT/file.txt","r")
# Read the file 
data = f.read()
print(data)
#Close the file 
f.close()

#The same can be written using with statement 
'''The with statement automatically closes the file after
 the block finishes, even if an error occurs.'''

with open("FILE_INPUT_OUTPUT/file.txt") as file:
    print(file.read())

