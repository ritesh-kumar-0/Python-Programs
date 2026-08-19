#getter method 
class Profile:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    # Getter method
    def getPassword(self):
        return self.__password


p1 = Profile("Ritesh", "2345")

# Get/read the private password
print(p1.getPassword())