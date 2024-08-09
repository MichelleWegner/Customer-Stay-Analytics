Customer Stay Analytics


This project focuses on predicting customer churn within a telecommunications company.
 By leveraging advanced machine learning techniques, we aim to identify key factors influencing churn and build a predictive model that can help the company proactively address customer retention.
  Through feature engineering, model development, hyperparameter tuning, and handling imbalanced data, the project culminates in an optimized model that provides actionable insights for business decisions.



## Dataset
The dataset used is the Telco Customer Churn dataset, which includes information on customer demographics, account details, and usage statistics. This data is instrumental in understanding customer behavior and predicting churn.

***Source: Kaggle - Telco Customer Churn Dataset***

***Dataset Features:***

Tenure Months: Duration (in months) that a customer has been with the company.
Monthly Charges: The monthly fee charged to the customer.
Total Charges: The cumulative charges incurred by the customer.
Churn Label: A binary indicator of whether the customer churned (1) or not (0).

Project Structure

The project is organized into the following stages:

1. Data Cleaning and Preparation
Addressed missing values and incorrect data formats.
Conducted feature engineering to create new variables such as TotalCharges_per_Month, improving the predictive power of the model.

2. Exploratory Data Analysis (EDA)
Visualized the distribution of key features to understand customer demographics and behavior.
Analyzed relationships between different variables and their impact on churn, providing a solid foundation for model development.

3. Handling Data Imbalance
Recognized and addressed class imbalance in the dataset using oversampling (e.g., SMOTE) and undersampling techniques.
Improved the model’s ability to detect both churn and non-churn customers by ensuring a balanced dataset during training.

4. Model Development
Implemented multiple machine learning models, including Logistic Regression, Random Forest, Support Vector Machine (SVM), and Gradient Boosting.
Initial evaluations were performed using confusion matrices and classification reports, setting the stage for further tuning.

5. Hyperparameter Tuning and Model Optimization
Applied Grid Search and Cross-Validation to fine-tune model parameters for optimal performance.

Identified Gradient Boosting as the best-performing model with the following parameters:

***learning_rate: 0.1***
***max_depth: 3***
***n_estimators: 100***


6. Model Evaluation

***The optimized Gradient Boosting model achieved an impressive accuracy of 92.83%.***

Comprehensive evaluation metrics, including confusion matrix, precision, recall, and F1-score, were used to validate the model’s effectiveness.
Results

# Best Model: GradientBoostingClassifier with an accuracy of 92.83%.
Key Insights:
Customers with month-to-month contracts are significantly more likely to churn than those with longer-term contracts.
Lower tenure and total charges are strong indicators of a customer’s likelihood to churn.

# Conclusion
The project successfully developed a robust model that not only delivers high accuracy but also provides balanced predictions for both churn and non-churn customers. The insights gained from the analysis can be used by the company to implement targeted retention strategies, ultimately reducing churn rates.

# Authors
This project was developed by Michelle & Sulaiman.

