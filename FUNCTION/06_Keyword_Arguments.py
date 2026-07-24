#Keyword Arguments 
'''In Keyword Arguments, we specify the parameter name while passing values.
The order does not matter.'''
# Function to dispaly student details 
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age = 20, name = "Ritesh")

#Python matches values using the parameter names, not their positions.