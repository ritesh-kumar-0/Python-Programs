#Set Operation 
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A) #{'Back in Black', 'Thriller', 'AC/DC'}

#We can add an element to a set using the add() method
A.add("Ritesh")
print(A)

#If we add the same element twice, nothing will happen as there can be no duplicates in a set
A.add("Ritesh")
print(A)

#We can remove an item from a set using the remove() method:
A.remove("Thriller")
print(A)

#We can verify if an element is in the set using the in command:
"Ritesh" in A
print(A)