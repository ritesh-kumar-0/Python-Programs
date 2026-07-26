# Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
#Return the converted value 
    return fahrenheit

celsius = float(input("Enter temperature in Celsius:"))

#Call the Function 
result = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit is:", result)
    