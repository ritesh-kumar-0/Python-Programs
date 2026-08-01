'''1. Write a program to read the text from a given file ‘poems.txtʼ and 
find out whether it contains the word ‘twinkleʼ.'''

#open the file in read mode 
file = open("FILE_INPUT_OUTPUT/poems.txt",)

#Read the entire file  content 
content = file.read()
#Check if the word "Twinkle " exixts in the file content 
if("Twinkle" in content):
    print("The word Twinkle is present in the content ")
else:
    print("The word Twinkle is not present in the content ")
#Close the
file.close()
