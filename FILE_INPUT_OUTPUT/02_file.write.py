#File Write 

str = "Hey ritesh you are good !"
#Open the file in Write mode 
f = open("myfile.txt", "w")
#Write a string to the file
f.write(str)
#close the file 

f.close()