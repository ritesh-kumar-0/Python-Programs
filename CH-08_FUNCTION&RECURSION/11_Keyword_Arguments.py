# **kwargs - Collecting keyword arguments 

def student(**details): # **details - collects arguments into a dictionary

#Loop through dictionary 
    for key , value in details.items():
        print(key, ":", value)

student(name="Ritesh", age = 19, course="BTech CSE")


    