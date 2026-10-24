import pandas as pd 

#load the csv file 
df = pd.read_csv("Product-sales.csv")

#Display the first 5 Rows 
print(df.head())

#Display the Number of rows and column 
print(df.shape)          

#Display all column Names 
print(df.columns)

#Check data Types and missing Values 
print(df.info())

#Display statistical summary 
print(df.describe())

# Display unique product 
print(df["Product"].unique)

#Count missing Values in each column 
print(df.isnull().sum())