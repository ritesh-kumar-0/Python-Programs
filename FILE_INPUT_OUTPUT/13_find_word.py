'''Write a program to mine a log file and find out whether it contains ‘pythonʼ.'''

#open the log file in red mode 
with open("FILE_INPUT_OUTPUT/log.txt", "r") as f:
    content = f.read() #reads the file

#text exists in file 
if ("Python" in content):
    print("Yes, the log file contains 'Python'.")
else:
    print("No the log file does not contains 'Python'.")


