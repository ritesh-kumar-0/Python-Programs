
words = ["Donkey", "bad","ganda"]

with open("FILE_INPUT_OUTPUT/filess.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word) )

with open("FILE_INPUT_OUTPUT/filess.txt", "w") as f:
    f.write(content)