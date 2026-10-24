'''loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select.
 This method includes the last element of the range passed in it.
 df.loc[row_label, column_label] row_label -> Which row u want , column_lablel -> column u want 
 
iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column.
 This method does not include the last element of the range passed in it. '''
import pandas as pd

#Define a dictionary data 
data = {'Name': ['Ritesh','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 
'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(data)
#Display the result 
print(df)

#Access the first row's Name using its label 
print(df.loc[0, 'Name'])   #Output: Ritesh

# Access the second row's salary 
print(df.loc[1, 'Salary'])  #Output: 80000

# Select Name and Salary column for all rows 
print(df.loc[ :,['Name', 'Salary']])

# Access the value on the first row and the first column
print(df.iloc[0,0])  #Output: Ritesh 

# Access the value on the first row and the third column
print(df.iloc[0 , 2])  #Output: Architect Group