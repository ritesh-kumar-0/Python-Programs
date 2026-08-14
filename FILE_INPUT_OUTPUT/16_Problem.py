'''Write a program to find out whether a file is identical
 and matches the content of another file'''

with open("FILE_INPUT_OUTPUT/file.txt", "r") as f:
    content1 = f.read()

with open("FILE_INPUT_OUTPUT/poems.txt", "r") as f:
    content2 = f.read()

if (content1 == content2):
    print("Both files are identical.")
else:
    print("Both files are not identical.")