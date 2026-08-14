'''Write a program to find out the line number where python is present from ques 6.'''

with open("FILE_INPUT_OUTPUT/log.txt", "r") as f:
    lines = f.readlines() #reads the file
line_no = 1
found = False
for line in lines:
    if ("Python" in line):
       print(f"Yes, Python is present at line number:{line_no}")
       found = True
    line_no += 1
if not found:
    print("No , Pyhon is not present !")