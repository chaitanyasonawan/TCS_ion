import pandas as pd
import matplotlib.pyplot as plt

# Correct file location
file_location = r"C:\Users\rawoo\Documents\Internship\salary_data.csv"

# Read the CSV file
df = pd.read_csv(file_location)

# Convert 'Current_Salary_in_Lakhs' to numeric and handle errors
df['Current_Salary_in_Lakhs'] = pd.to_numeric(df['Current_Salary_in_Lakhs'].str.replace(' lakhs', ''), errors='coerce')

# Drop rows with NaN values in 'Current_Salary_in_Lakhs'
df = df.dropna(subset=['Current_Salary_in_Lakhs'])

# Plot the histogram with a different style
plt.figure(figsize=(12, 8))
plt.hist(df['Current_Salary_in_Lakhs'], bins=20, edgecolor='black', color='blue', alpha=0.7)
plt.title('Current Salary Distribution (in Lakhs)', fontsize=15)
plt.xlabel('Current Salary in Lakhs', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', alpha=0.75)
plt.show()
