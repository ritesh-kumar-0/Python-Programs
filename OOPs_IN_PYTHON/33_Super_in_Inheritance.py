#super() In Inheritance 
'''super() is used to call a method or constructor of the parent class'''
class Parent:

    def __init__(self):
        print("Parent constructor")


class Child(Parent):

    def __init__(self):

        # Calling parent constructor
        super().__init__()

        print("Child constructor")


obj = Child()