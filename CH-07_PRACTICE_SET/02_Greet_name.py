# Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
#l = ["Ritesh", "Soham", "Sachin", "Bahul"]

l = ["Ritesh", "Soham", "Sachin", "Bahul"] 

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")