#working with two product details.

#Create an empty dictionary 
inventory = {}

#Store the first product details in variable
''' 1: Product Name= Mobile phone
       Product Quantity= 5
       Product price= 20000
       Product Release Year= 2020 '''
#Product details 
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

#Store product details in inventory 

inventory["ProductNo1"] = {
    "name" : ProductNo1,
    "quantity" : ProductNo1_quantity,
    "price" : ProductNo1_price,
    "releaseYear" : ProductNo1_releaseYear

}
print("First Product details")
print(inventory)

#Store the second product details in variable
'''Product Name= "Laptop"
   Product Quantity= 10
   Product price = 50000
   Product Release Year= 2023'''

#Product details 
ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023

#Store Second product details in inventory

inventory["ProductNo2"] = {
    "name" : ProductNo2, 
    "quantity" : 10,
    "price" : 50000,
    "releaseYear" : 2023
}

print("\nSecond Product Details")
print(inventory["ProductNo2"])

#Display the Products present in the inventory
print(inventory)

if "releaseYear" in inventory["ProductNo1"]:
    print(f"ProductNo1 release year is in {ProductNo1_releaseYear}")

if "releaseYear" in inventory["ProductNo2"]:
    print(f"ProductNo2 release year is in {ProductNo2_releaseYear}")