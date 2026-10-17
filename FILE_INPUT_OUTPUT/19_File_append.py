#Appending the data to an existing file 
# Data to append to the existing file
new_data = "\nRitesh Play Cricket "

#open existing file for appending \
with open ('file.txt', 'a') as file1:
    file1.write(new_data + "\n")
     # file1 is automatically closed when the 'with' block exits