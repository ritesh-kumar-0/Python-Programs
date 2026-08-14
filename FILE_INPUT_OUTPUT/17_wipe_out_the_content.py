'''Write a program to wipe out the content of a file using python'''

with open("FILE_INPUT_OUTPUT/myfile.txt", "w") as f:
    f.write("")

print("File content has been wiped out.")