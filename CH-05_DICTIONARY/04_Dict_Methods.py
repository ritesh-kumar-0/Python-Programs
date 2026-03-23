
marks = {
    "Ritesh": 99,
    "Kundan": 88,
    "Aryan": 23
}
#Returns a list of(Key, Value) tuples
print(marks.items())
#Rerurns a list containing dictionary's keys
print(marks.keys())

#returns values of keys
print(marks.values())     #dict_values([99, 88, 23])

#Update the dictionary with supplied key-value pairs
marks.update({"Ritesh": 98})
print(marks)            #{'Ritesh': 98, 'Kundan': 88, 'Aryan': 23}

#Returns the value of the specified keys
print(marks.get("Ritesh"))     # 98

#Difference between 

print(marks.get("Ritesh1")) #prints None  
print(marks["Ritesh"])  #Returns an Error