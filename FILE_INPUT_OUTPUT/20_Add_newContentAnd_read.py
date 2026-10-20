# a+ adds new content at the end and allows reading 
with open("FILE_INPUT_OUTPUT/newfile.txt", 'a+') as testwritefile:
    testwritefile.write("\nThis is line E\n")
    print(testwritefile.read())