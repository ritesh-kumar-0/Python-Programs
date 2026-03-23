# Adding Elements In Set 

fruits = {"Apple", "Banana", "Cherry", "Grapes"}

#using add() -> Adds a single elements to the set 
fruits.add("AALU")
print(fruits)     # output: {'Cherry', 'Grapes', 'Apple', 'AALU', 'Banana'}

# update() -> add multiple elements at once 
fruits.update(["Mango","Tato"])
print(fruits)