#Exclusive Create Mode (x)
'''Creates a new file only.
If the file already exists, Python raises an error.'''

f = open("FILE_INPUT_OUTPUT/newfile.txt", "x")

#Write the text "Hello Ritesh" into the file
f.write("Hello Ritesh ")
#close the file save the changes 
f.close()
#Dispaly message 
print("File created successfully! ")