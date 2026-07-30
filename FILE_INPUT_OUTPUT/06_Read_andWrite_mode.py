#Read and Write mode (r+)
#Allows both reading and writing.File must already exist

file = open("FILE_INPUT_OUTPUT/newfile.txt", "r+")
print(file.read())
file.write("How Are You?")
file.close()