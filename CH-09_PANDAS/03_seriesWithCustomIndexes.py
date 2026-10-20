# Series with custom indexes 
import pandas as pd 

# Create a Series with student names as index labels
marks = pd.Series([80, 90, 75],  # values stored in the series 
        index = ["Ritesh", "Aman", "Ankush"]) # Custom index labels 

#Display the series 
print(marks)    

#Access the marks using the student index label 
print(marks.loc["Ankush"])

#Access the first value by its integer position 
print(marks.iloc[0])

