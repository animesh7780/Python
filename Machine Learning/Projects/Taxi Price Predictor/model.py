import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

# Load dataset
data = pd.read_csv('taxi_trip_pricing.csv')

# Select features and target
features = ['Trip_Distance_km', 'Passenger_Count', 'Base_Fare', 'Per_Km_Rate', 'Per_Minute_Rate', 'Trip_Duration_Minutes']
target = ['Trip_Price']

# Split data into training and testing sets
X_train = data[features][:-30]
X_test = data[features][-30:]
Y_train = data[target][:-30]
Y_test = data[target][-30:]

# Handle missing values in X_train and X_test
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
Y_train = imputer.fit_transform(Y_train)
Y_test = imputer.transform(Y_test)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions
Y_predicted = model.predict(X_test)

# Custom input values for prediction
custom_input = np.array([[19.35, 3, 3.56, 0.8, 0.32, 53.82]])  

print("Custom input shape:", custom_input.shape) 

custom_prediction = model.predict(custom_input)

print("Predicted Trip Price:", custom_prediction[0])

