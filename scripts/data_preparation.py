# data_preparation.py

import pandas as pd

def load_data(file_path):
    data = pd.read_excel(file_path, engine='openpyxl')
    return data

def clean_data(data):
    # Handling missing values
    data['Total Charges'] = pd.to_numeric(data['Total Charges'], errors='coerce')

    # Separate numerical and categorical columns
    numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    categorical_columns = data.select_dtypes(include=[object]).columns.tolist()

    # Fill missing values for numerical columns with median
    from sklearn.impute import SimpleImputer
    imputer_num = SimpleImputer(strategy='median')
    data[numerical_columns] = imputer_num.fit_transform(data[numerical_columns])

    # Encoding categorical variables
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for column in categorical_columns:
        if column not in ['CustomerID', 'Churn Reason']:
            data[column] = le.fit_transform(data[column])

    # Feature engineering
    # Prevent division by zero by replacing zeroes with NaN in 'Tenure Months'
    data['Tenure Months'].replace(0, pd.NA, inplace=True)
    data['TotalCharges_per_Month'] = data['Total Charges'] / data['Tenure Months']

    # Replace infinite values with NaN
    data.replace([float('inf'), float('-inf')], pd.NA, inplace=True)

    # Impute remaining missing values
    data[numerical_columns] = imputer_num.fit_transform(data[numerical_columns])

    # Normalize numerical features
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numerical_features = ['Tenure Months', 'Monthly Charges', 'Total Charges', 'TotalCharges_per_Month']
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    # Dropping unnecessary columns
    data.drop(['CustomerID', 'Churn Reason'], axis=1, inplace=True)

    return data

def save_cleaned_data(data, output_path):
    data.to_csv(output_path, index=False)
    print("Dataset successfully prepared and saved.")
