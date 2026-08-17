'''Q3: 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
‘object.a = 0ʼ. Does this change the class attribute?'''

class Test:
    a = 10  #class attribute 

object = Test()

print("Before changing:")
print("Class attribute:", Test.a)
print("Object attribute:", object.a)


# Set a directly using the object
object.a = 0  #Python creates a inside the object.

print("\nAfter changing:")
print("Class attribute:", Test.a)
print("Object attribute:", object.a)

'''When you write object.a = 0 , Python generally searches 1.Object -> 2.Class
If the object doesn't have a, Python gets it from the class'''