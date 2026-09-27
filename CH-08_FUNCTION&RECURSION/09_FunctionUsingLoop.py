#Using loops in Function 

def printStuff(Stuff):
    for i, s in enumerate(Stuff): # i = index Number , s = value from the list 
        print("Album", i , "Rating is ", s)

#Function call 
# This is a list containing album rating 
album_ratings = [10.0 , 8.5, 9.5]
printStuff(album_ratings) # send the list to the printStuff()