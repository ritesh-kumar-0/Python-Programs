#Suppose we want to calculate the length of a string

#Without Walrus
"""text = "Python Programming"

if len(text) > 10:
    print(len(text))  # Output : 18 """

#With walrus 
if(len := len("Python Programming")) > 10:
    print(len)
