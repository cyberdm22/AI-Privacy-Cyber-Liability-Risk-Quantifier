import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

print("Loading dataset and initializing preprocessing...")

# 1. Load the processed dataset
df = pd.read_csv('financial_risk_assessment.csv')

# 2. Feature Engineering (One-Hot Encoding)
# Machine Learning algorithms cannot perform math on text strings like 'SQL_Injection'. 
# We use pd.get_dummies to convert categorical columns into binary (1 or 0) matrices.
features = df.drop(columns=[
    'App_ID', 
    'Operational_Loss_INR', 
    'Statutory_Fine_INR', 
    'Total_Liability_INR', 
    'Penalty_Mitigation_Percentage', 
    'Insurance_Readiness_Score'
])
X = pd.get_dummies(features)

# Our Target Variable (y) is what the model is trying to predict: The Total Financial Liability
y = df['Total_Liability_INR']

# 3. Train/Test Split
# We split the data: 80% for the model to learn the underlying patterns, 20% to test its true accuracy on unseen data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Hyper-parameter Configuration
# n_estimators = 100: The 'Forest' will consist of 100 independent decision trees.
# max_depth = 10: We restrict how deep each tree can grow to prevent overfitting (memorizing the training data).
print("Training the Random Forest Regressor...")
rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

# 5. Model Training
rf_model.fit(X_train, y_train)

# 6. Model Prediction & Evaluation
y_train_pred = rf_model.predict(X_train)
y_test_pred = rf_model.predict(X_test)

# 7. Calculating Error Metrics (RMSE and R-Squared)
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

# 8. Output the Academic Metrics for the Research Report
print("\n--- AI Model Performance Metrics ---")
print(f"Training R-Squared: {train_r2:.4f}")
print(f"Testing R-Squared:  {test_r2:.4f}")
print(f"Training RMSE:      ₹{train_rmse:,.2f}")
print(f"Testing RMSE:       ₹{test_rmse:,.2f}")

# Save the trained model structure to the hard drive for Phase 2 (Deployment)
joblib.dump(rf_model, 'financial_risk_model.pkl')
# Also save the feature columns structure so future inputs match the training schema
joblib.dump(X.columns, 'model_features.pkl')

print("\nModel successfully compiled and saved as 'financial_risk_model.pkl'")
