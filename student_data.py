import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv(r"C:\Users\anind\OneDrive\Desktop\PythonVSC\Practice\student_data.csv")

'''Create a NumPy array of student ages and calculate: Mean, Median, Standard Deviation
arr = np.array([1,2,8,9,5,6])
print("Mean Value is :", np.mean(arr))
print("Median Value is :", np.median(arr))
print("Standerd Derivation Value is :", np.std(arr))'''


'''Extract students who study more than 5 hours/day using NumPy only (not pandas). using Boolean Masking
# Get the column index number of "Study_Hours_per_Day"
# (NumPy does not understand column names, only index numbers)
col_index = df.columns.get_loc("Study_Hours_per_Day")
# Convert the pandas DataFrame into a NumPy array
# After this, df becomes a 2D array (rows and columns)
df = df.to_numpy()
# Create a condition:
# df[:, col_index]  → Take ALL rows (:) and only the Study_Hours column
# > 5               → Check which students study more than 5 hours
# This creates a Boolean mask like [True, False, True, ...]
filtered_students = df[df[:, col_index] > 5]
print("Students who study more than 5 hours/day:\n", filtered_students)'''


'''Min-Max Normalization
# Convert Final_Score column to NumPy array
scores = df["Final_Score"].to_numpy()
# Find min and max
min_val = np.min(scores)
max_val = np.max(scores)
# Apply Min-Max Normalization formula
normalized_scores = (scores - min_val) / (max_val - min_val)
print("Normalized Final Scores:\n", normalized_scores)'''


'''Find top 5 highest Final Scores using NumPy
# Convert Final_Score column to NumPy array
scores = df["Final_Score"].to_numpy()
sorted_scores = np.sort(scores)
print("Top 5 marks is :",sorted_scores[-5:])'''


'''Basic Dataset Overview & Check how many missing values each column has
print(df.head(10))
print(df.tail(5))
print(df.columns)
print(df.shape)
print(df.isnull().sum())'''


'''Find average Final Score for: Male students, Female students
Diff = (df.groupby("Gender")["Final_Score"].mean())
print("Final score of Male & Female both is : \n", Diff)'''


'''Conditional Filtering Find students who: Sleep < 5 hours AND score > 80
sorted_student = df[(df["Sleep_Hours"] < 5) & (df["Final_Score"] > 80)]
print(sorted_student)'''


'''Create New Column Create: Total_Score = Midterm_Score + Final_Score
df["Total_Score"] = df["Midterm_Score"] + df["Final_Score"]
print(df.head(5))'''


'''Top 10 Students by Final Score, Sort students by Final Score (highest first) and show top 10.
df.sort_values(by="Final_Score", ascending=False)
print(df.head(11))'''

'''Find percentage of Pass vs Fail
df["Pass_or_Fail"].value_counts(normalize=True)
print(df)'''


