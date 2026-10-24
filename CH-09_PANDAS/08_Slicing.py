#Slicing uses the [] operator to select a set of rows and/or columns from a DataFrame
#To slice out a set of rows, you use this syntax: data[start:stop],
import pandas as pd

#Define a dictionary data 
data = {'Name': ['Ritesh','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 
'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(data)

# Do slicing 
print(df.iloc[0:2, 0:3])

#let us do the slicing using loc() function on  df where index column is having labels as 0,1,2
print(df.loc[0:2,'ID':'Department'])

