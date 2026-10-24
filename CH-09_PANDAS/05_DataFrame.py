'''A DataFrame is a two-dimensional, labeled data structure in Pandas that stores data in rows and columns.
 Each column can contain a different data type.'''
import pandas as pd

#Define a dictionary data 
data = {'Name': ['Ritesh','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 
'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(data)
#Display the result 
print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(x)

#check the type of x
print(type(x))  # output : <class 'pandas.DataFrame'>