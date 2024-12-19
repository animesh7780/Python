import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('pollution_dataset.csv')

#replace categorical values with numerical
df.replace({'Air_Quality': {'Good': 0, 'Moderate': 1, 'Poor': 2, 'Hazardous': 3}}, inplace=True)

X =  df[['Temperature','Humidity', 'SO2', 'NO2', 'CO', 'PM10', 'PM2.5','Proximity_to_Industrial_Areas','Population_Density']]
y = df['Air Quality']

# Split data into training and testing sets
X_train = X[:-30]
X_test = X[-30:]
y_train = y[:-30]
y_test = y[-30:]

# Initialize and train the model
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# Make predictions
y_predicted = model.predict(X_test)

# Custom input values for prediction
custom_input = np.array([[20,53.3,3.7,12.9,26.1,6.6,1.09,10.2,538]])
custom_prediction = model.predict(custom_input)
print("Predicted Air Quality:", custom_prediction[0])