#String Slicing 

name = "Ritesh Kumar"

print("ORIGINAL STRING:", name )
print("_" *30)


#Full string 
print("Full String:",name[:])

# From index 0 to 3 (end excluded)
print("1. name[0:3]        :", name[0:3])  #Rit

# From index 2 to end
print("2. name[2:]         :", name[2:])   #tesh Kumar

#  From start to index 4 (end excluded)
print("3. name[:4]         :", name[:4])  #Rite

# Last character (negative index)
print("4. Last Character    :", name[-1]) # r

# Reverse string
print("5. Reverse          :", name[::-1]) #ramuK hsetiR

#  Every 2nd character (step = 2)
print("6. name[::2]        :", name[::2])  #Rts ua

#  Reverse with step 2
print("7. name[::-2]       :", name[::-2])  # rmKhei

#  Negative indexing slice
print("8. name[-4:-1]      :", name[-4:-1]) # uma

#  Custom slicing (start:end:step)
print("9. name[1:5:2]     :", name[1:5:2]) # ie