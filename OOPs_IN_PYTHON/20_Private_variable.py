#Private variable __

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #Private attribute(variable ) 

    def getBalance(self):
        return self.__balance # Getter method used


account1 = BankAccount("Ritesh", 11100)
# Changing the public attribute
account1.name = "Shayam"
print(account1.name)
# Call getBalance() to access the private balance
print(account1.getBalance())
        