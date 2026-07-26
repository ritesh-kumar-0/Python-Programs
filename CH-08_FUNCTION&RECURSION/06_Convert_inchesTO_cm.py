#Write a python function which converts inches to cms.

def inches_cms(inches):
   #Formula to convert inches to cms
   cms  =  inches * 2.54
   return cms

#user input 
inches = float(input("Enter lenth in inches: "))

#Call the function 
result = inches_cms(inches)
print("Length in centimeters is : ",result,"cm")
