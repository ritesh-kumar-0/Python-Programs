# Set name as the index 
'''Q:When should you set Name as the index? 
    Ans -> '''

import pandas as pd

#Define a dictionary data 
data = {'Name': ['Ritesh','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': [' Software Group', 
'Architect Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(data)
#Display the result 
print(df)

# Set Name as the index 
df = df.set_index('Name')

#Select the Ritesh Complete row 
print(df.loc['Ritesh'])

#Access the Ritesh ID 
print(df.loc['Ritesh', 'ID'])  # Output: 1

# Select rows from Ritesh to Jane
print(df.loc['Ritesh':'Jane'])



