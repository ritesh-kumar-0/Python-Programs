'''A file is used to store data permanently so that it can be
 accessed even after the program ends.'''
#File read 

#Open the file 
f = open("FILE_INPUT_OUTPUT/file.txt", "r")
# Read the file 
data = f.read()
print(data)
#Close the file 
f.close()