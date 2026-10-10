#What happens when keys are same 

student1 = {
    "name": "Ritesh",
    "age": 20
}

student2 = {
    "age": 21,
    "course": "CSE"
}

student = student1 | student2
print(student)  #{'name': 'Ritesh', 'age': 21, 'course': 'CSE'}

# Why? - Because both dictionaries have "age" 
#Rule -> When duplicate keys exist, the right-hand dictionary's value replaces the left-hand value.
