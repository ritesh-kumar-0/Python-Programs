#@property 

class Student:
    def __init__(self, name, __marks):
        self.name = name
# Store marks as a private variable
        self.__marks = __marks

#Getter
    @property  # it allows us to access marks like a normal attribute
    def marks(self):
        return self.__marks

#setter
#This method is called when we assign a new value to marks
    @marks.setter
    def marks(self, new_marks):
        if not 0 <= new_marks <= 100:
            print("Invaild Marks")
            return
        self.__marks = new_marks #update the marks 

s1 = Student ("Ritesh", 100)
print(s1.marks) #Getter is automatically called 

s1.marks = 99
print(s1.marks)