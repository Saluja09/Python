# -*- coding: utf-8 -*-
"""XGBoost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pSKXz7lT3tn4CHUssMZ7uLuvNcogrwAT
"""

# Import necessary libraries
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset for classification
data = load_iris()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create an XGBoost classifier
model = xgb.XGBClassifier(
    objective='multi:softmax',  # For multi-class classification
    num_class=3,  # Number of classes in the target variable
    max_depth=3,  # Maximum depth of each tree
    learning_rate=0.1,  # Step size shrinkage to prevent overfitting
    n_estimators=100  # Number of boosting rounds
)

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Example Usage:
# You can use the trained model to make predictions for new data points.
# For example, let's create a sample input and predict its class label.
sample_input = [[5.1, 3.5, 1.4, 0.2]]  # Replace with your input data
predicted_class = model.predict(sample_input)[0]

print(f"Predicted class label for the sample input: {predicted_class}")

# You can also inspect feature importance to understand which features are most influential.
feature_importance = model.feature_importances_
print("Feature Importance:")
for i, importance in enumerate(feature_importance):
    print(f"Feature {i+1}: {importance}")