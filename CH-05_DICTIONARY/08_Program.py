'''a) Create a dictionary album_sales_dict where the keys are the album name and the sales 
in millions are the values.'''
album_sales_dict = {"Back in Black" : 50, "The Bodyguard" : 50, "Thriller" : 65 }

#b) Use the dictionary to find the total sales of Thriller:
print(album_sales_dict["Thriller"]) #65

#c) Find the names of the albums from the dictionary using the method keys():
print(album_sales_dict.keys()) #dict_keys(['Back in Black', 'The Bodyguard', 'Thriller'])

#d) Find the values of the recording sales from the dictionary using the method values:
print(album_sales_dict.values()) #dict_values([50, 50, 65])
