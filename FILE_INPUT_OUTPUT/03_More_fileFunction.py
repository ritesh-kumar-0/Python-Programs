# open the file 
f = open("FILE_INPUT_OUTPUT/file.txt")

lines = f.readlines()
print(lines, type(lines))
f.close()