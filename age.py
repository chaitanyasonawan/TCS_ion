import pandas as pd
import matplotlib.pyplot as plt

# Correct file location
file_location = r"C:\Users\rawoo\Documents\Internship\salary_data.csv"

# Read the CSV file
df = pd.read_csv(file_location)

# Convert 'Age' to numeric and handle errors
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Drop rows with NaN values in 'Age'
df = df.dropna(subset=['Age'])

# Plot the age distribution as a histogram with blue color
plt.figure(figsize=(12, 7))
plt.hist(df['Age'], bins=30, edgecolor='white', color='blue', alpha=0.7)
plt.title('Age Distribution of Employees', fontsize=15)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', alpha=0.75)
plt.show()
