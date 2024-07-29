import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load the saved model and label encoder
model = joblib.load('model.pkl')
le = joblib.load('le.pkl')

# Load and preprocess the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    if 'Job_Title' not in data.columns or 'Current_Salary_in_Lakhs' not in data.columns:
        raise ValueError("CSV file must contain 'Job_Title' and 'Current_Salary_in_Lakhs' columns.")
    
    data['Job_Title'] = le.transform(data['Job_Title'])
    
    # Remove ' lakhs' and convert salary to float
    data['Current_Salary_in_Lakhs'] = data['Current_Salary_in_Lakhs'].str.replace(' lakhs', '').astype(float)
    
    X = data[['Age', 'Years_of_Experience', 'Job_Title']]
    y = data['Current_Salary_in_Lakhs']
    
    return X, y

# Evaluate the model and visualize predictions
def evaluate_model(csv_file):
    X, y = load_data(csv_file)
    y_pred = model.predict(X)
    
    # Visualize the predicted salaries using a histogram
    plt.figure(figsize=(12, 8))
    plt.hist(y_pred, bins=20, edgecolor='black', color='blue', alpha=0.7)
    plt.title('Predicted Salary Distribution (in Lakhs)', fontsize=15)
    plt.xlabel('Predicted Salary in Lakhs', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Main function
if __name__ == "__main__":
    csv_file = r"C:\Users\rawoo\Documents\Internship\salary_data.csv"
    evaluate_model(csv_file)
