#Setter method
class Profile:

    def __init__(self, name, password):
        # Store the name as a public attribute
        self.name = name

        # Store password as a private attribute
        self.__password = password

    # Setter method
    def setNewPassword(self, new_password):

        # Update the private password with the new password
        self.__password = new_password

        # Display confirmation message
        print("Password Updated")


# Create an object of Profile
p1 = Profile("Ritesh", "2345")

# Call the setter method to change the password
p1.setNewPassword("56676")