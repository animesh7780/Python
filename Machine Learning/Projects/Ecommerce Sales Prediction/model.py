import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score

# Load dataset
data = pd.read_csv('Sales_data.csv')

# Define features and target
categorical_columns = ['Product_Category', 'Customer_Segment']
numeric_columns = ['Price', 'Discount', 'Marketing_Spend']
X = data[numeric_columns + categorical_columns]
y = data['Units_Sold']

# Create preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_columns),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_columns)
    ])

# Create a pipeline with preprocessing and SVR
svr_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', SVR(kernel='linear', C=1.0, epsilon=0.1))
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the pipeline
svr_pipeline.fit(X_train, y_train)

# Make predictions
y_pred = svr_pipeline.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Perform cross-validation
cv_scores = cross_val_score(svr_pipeline, X, y, cv=5, scoring='r2')
print("\nCross-validation R2 scores:", cv_scores)
print("Mean CV R2 score:", cv_scores.mean())

# Optional: Feature importance analysis
# Get feature names after preprocessing
feature_names = (
    preprocessor
    .named_transformers_['cat']
    .get_feature_names_out(categorical_columns).tolist() + 
    numeric_columns
)

# Extract coefficients 
coefficients = svr_pipeline.named_steps['regressor'].coef_[0]

# Create feature importance DataFrame
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': np.abs(coefficients)
}).sort_values('importance', ascending=False)

print("\nFeature Importances:")
print(feature_importance)

#prediciting sales
new_data = pd.DataFrame({
    'Price': [932.8],
    'Discount': [35.82],
    'Marketing_Spend': [6780.38],
    'Product_Category': ['Sports'],
    'Customer_Segment': ['Premium']
})

predicted_sales = svr_pipeline.predict(new_data)
print("\nPredicted Sales:", predicted_sales[0])