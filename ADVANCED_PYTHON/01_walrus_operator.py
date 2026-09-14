#WALRUS OPERATOR 
'''The Walrus Operator (:=) is an assignment expression introduced in Python 3.8.
It allows you to assign a value to a variable and use that value in the same expression'''

if (name := input("Enter your name: ")):
    print("Hello", name)
