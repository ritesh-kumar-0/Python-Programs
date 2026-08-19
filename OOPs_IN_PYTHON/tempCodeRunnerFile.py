#Private variable __

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #Private variable 

    def getBalance(self):
        return self.__balance


account1 = BankAccount("Ritesh", 11100)
account1.name = "Shayam"
print(account1.name)
print(account1.getBalance())
        