import seaborn as sns
import matplotlib.pyplot as plt

def plot_churn_distribution(data):
    sns.countplot(x='Churn Label', data=data)
    plt.title('Distribution of Churn')
    plt.show()

def plot_pairplot(data, key_features):
    sns.pairplot(data[key_features + ['Churn Label']], hue='Churn Label', diag_kind='kde')
    plt.show()

def plot_boxplot(data, x, y, title):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x, y=y, data=data)
    plt.title(title)
    plt.show()

def plot_scatter(data, x, y, hue, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, hue=hue, data=data)
    plt.title(title)
    plt.show()


