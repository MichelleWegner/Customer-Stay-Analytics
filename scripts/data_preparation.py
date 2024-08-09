import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(csv_file_path):
    try:
        data = pd.read_excel(csv_file_path)
        print("File read successfully as a CSV file.")
        return data
    except FileNotFoundError:
        print(f"The file at {csv_file_path} was not found. Please check the file path and try again.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

def clean_data(data):
    # Replace missing values in 'Total Charges'
    data['Total Charges'] = pd.to_numeric(data['Total Charges'], errors='coerce')
    data['Total Charges'] = data['Total Charges'].fillna(data['Total Charges'].median())

    # Encode categorical variables
    le = LabelEncoder()
    for column in data.select_dtypes(include=['object']).columns:
        data[column] = le.fit_transform(data[column])

    # Normalize numerical features
    scaler = StandardScaler()
    numerical_features = ['Monthly Charges', 'Total Charges']
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    return data

def prepare_data(data):
    # Handle missing values
    imputer = SimpleImputer(strategy='median')
    data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

    # Feature engineering
    data['TotalCharges_per_Month'] = data['Total Charges'] / data['Tenure Months']
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    return data