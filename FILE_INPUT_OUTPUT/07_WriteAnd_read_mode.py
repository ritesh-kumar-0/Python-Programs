#Write and read Mode 
#Allows reading and writing. Deletes existing data first

file = open("FILE_INPUT_OUTPUT/newfile.txt", "w+")
# Write text into the file
file.write("IM Ritesh")
# Move the file pointer to the beginning (position 0)
# Otherwise read() will return an empty string.
file.seek(0)
# Read and print the file content
print(file.read())
file.close()

#What will happen if seek(0) is removed?
'''ANS - (Empty string)
Reason: After write(), the file pointer is already at the end of
 the file, so read() has nothing left to read.'''