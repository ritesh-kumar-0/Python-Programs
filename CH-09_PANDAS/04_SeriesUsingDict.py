#Series using Dictionary: 

import pandas as pd  # Import the pandas library

# Create a dictionary containing student marks
data = {
    "Ritesh": 85,
    "Rohit": 90,
    "Khundan": 95,
    "Rahul": 80
}

# Convert the dictionary into a Pandas Series
series = pd.Series(data)

# Print the complete Series
print(series)

# Print the index labels
print(series.index)

# Print the values of the Series
print(series.values)