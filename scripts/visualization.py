# visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Churn Label', y='Monthly Charges', data=data)
    plt.title('Monthly Charges Distribution for Churn and Non-Churn Customers')
    plt.xlabel('Churn Label')
    plt.ylabel('Monthly Charges')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Churn Label', y='Total Charges', data=data)
    plt.title('Total Charges Distribution for Churn and Non-Churn Customers')
    plt.xlabel('Churn Label')
    plt.ylabel('Total Charges')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Churn Label', y='Tenure Months', data=data)
    plt.title('Tenure Distribution for Churn and Non-Churn Customers')
    plt.xlabel('Churn Label')
    plt.ylabel('Tenure Months')
    plt.show()

