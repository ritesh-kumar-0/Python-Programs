# Removing Elements from a set 

fruits = {"Apple", "Banana", "Cherry", "Grapes"}

#1.remove(element) -> Removes a specific element
# Gives an Error if element not found 
fruits.remove("Apple")
print(fruits)    #{'Grapes', 'Cherry', 'Banana'}

#2.discard(Element)->Removes a specific element
#No Error if element does't exist
fruits.discard("Cherry")
print(fruits)         #{'Grapes', 'Banana'}

#3. pop()  -> Removes and return a random element(Since set is unordered)
item = fruits.pop()
print("Removed:" , item)
print(fruits)     #Removed: Banana

#4. clear() -> removes all elements from the set 
fruits.clear()
print(fruits)     #set()