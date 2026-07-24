#Can a function have both print()and return?
#ANS- Yes

def add(a, b):
    print("Adding numbers...")
    return a + b
result = add(10 , 20)
print(result)

#Here, print() display a message ,while return sends the ans back
