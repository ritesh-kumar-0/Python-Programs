#Multiple Inheritance 
'''When one child class inherits from multiple parent classes.'''
# First parent
class Father:

    def father_property(self):
        print("Father's property")


# Second parent
class Mother:

    def mother_property(self):
        print("Mother's property")


# Child class
class Child(Father, Mother):

    def child_property(self):
        print("Child's property")


# Object
c = Child()

c.father_property()
c.mother_property()
c.child_property()