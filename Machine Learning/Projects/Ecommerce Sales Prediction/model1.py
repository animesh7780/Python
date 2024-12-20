import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('Sales_data.csv')

# Replace categorical values with numerical codes
data.replace({
    'Product_Category': {
        'Sports': 0,
        'Toys': 1,
        'Home Decor': 2,
        'Fashion': 3,
        'Electronics': 4
    },
    'Customer_Segment': {
        'Occasional': 0,
        'Regular': 1,
        'Premium': 2
    }
}, inplace=True)

# Define feature matrix (X) and target vector (y)
X = data[['Price', 'Discount', 'Marketing_Spend', 'Product_Category', 'Customer_Segment']]
y = data['Units_Sold']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor  
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions on test data
y_pred = rf.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)

# Example new data for prediction
new_data = pd.DataFrame({
    'Price': [569],
    'Discount': [3],
    'Marketing_Spend': [6807],
    'Product_Category': [1],
    'Customer_Segment': [2]
})

# Predict sales for the new data
predicted_sales = rf.predict(new_data)
print("Predicted Sales:", predicted_sales)
