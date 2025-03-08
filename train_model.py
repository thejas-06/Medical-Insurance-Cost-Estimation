import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load dataset (ensure 'insurance.csv' is in your project folder)
df = pd.read_csv("insurance.csv")
print(df.head())

# Preprocess the data:
# For the insurance dataset, typical features include: age, sex, bmi, children, smoker, region, charges
# We want to predict 'charges' using the other features.
# Convert categorical features into numerical values via one-hot encoding.
df_processed = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)

# Separate features and target variable
X = df_processed.drop("charges", axis=1)
y = df_processed["charges"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model using Mean Squared Error
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Save the trained model to a file
joblib.dump(model, "model.pkl")
