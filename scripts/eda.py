# eda.py

import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(data):
    sns.countplot(x='Churn Label', data=data)
    plt.title('Distribution of Churn')
    plt.show()
    
    sns.pairplot(data, hue='Churn Label', diag_kind='kde')
    plt.show()

