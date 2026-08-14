'''Write a program to make a copy of a text file “this.txt”'''

#open original file in read mode
with open("FILE_INPUT_OUTPUT/this.txt", "r") as f:
    content = f.read()

#creates a new file in write mode.
with open("copey.txt", "w") as f:
    f.write(content)   #writes the same content into copy.txt.

print("File copied successfully! ")