'''A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file'''
word = "Donkey"

with open("FILE_INPUT_OUTPUT/filess.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("FILE_INPUT_OUTPUT/filess.txt", "w") as f:
    f.write(contentNew)