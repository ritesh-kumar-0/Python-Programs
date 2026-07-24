# Function with default electricity rate
def bill(units, rate=8):

    total = units * rate

    print("Total Bill =", total)

# Take units from the user
units = int(input("Enter electricity units: "))

# Call function
bill(units)