#Dictionary Merge Operator  |
# The | operator merges two dictionaries and returns a new dictionary.
student = {
    "name": "Ritesh",
    "age": 20
}

course = {
    "course": "BTech CSE",
    "year": 1
}

result = student | course 
print(result)  #Output: {'name': 'Ritesh', 'age': 20, 'course': 'BTech CSE', 'year': 1}

#Important: student and course themselves are not changed.