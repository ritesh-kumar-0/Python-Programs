#Write a function student_info() that accepts any number of student details using **kwargs and prints them.
'''student_info(
    name="Ritesh",
    age=20,
    course="BTech CSE",
    university="Shoolini"
)'''

# **kwargs collects all keyword arguments into a dictionary 
def student_info(**kwargs):

    for key, value in kwargs.items(): 
        print(key, ":", value)  # print each kay and list 

#calling the function 
student_info(
    name = "Ritesh",
    age = 20,
    course = "BTech CSE",
    university = "Shoolini",
)