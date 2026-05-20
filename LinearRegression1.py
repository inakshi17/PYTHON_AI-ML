import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
try:
    df = pd.read_csv('property_data.csv')
except FileNotFoundError:
    print("CSV not found, generating dummy data...")
    data = {
        'Square_Footage': [1500, 2000, np.nan, 2500, 1800, 3000, 2200, 1600],
        'Number_of_Rooms': [3, 4, 3, 5, 3, 6, 4, 3],
        'Distance_to_City_Center': [5, 10, 15, 2, 7, 20, 8, 12],
        'Crime_Rate_Index': [1.2, 2.5, 0.5, 3.1, 1.8, 0.2, 1.5, 2.0],
        'Property_Tax': [3000, 4500, 2800, 5500, 3200, 6000, 4800, 3100]
    }
    df = pd.DataFrame(data)

df = df.fillna(df.mean())

X = df.drop('Property_Tax', axis=1)
y = df['Property_Tax']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_spli
model = LinearRegression()
model.fit(X_train, y_train)

print("--- Model Parameters ---")
print(f"Intercept: {model.intercept_:.2f}")

coeffs = pd.Series(model.coef_, index=X.columns)
print("\nCoefficients for each feature:")
print(coeffs)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\nRoot Mean Squared Error (RMSE): {rmse:.2f}")

print("\n--- Predict Property Tax for New Data ---")
user_input = []
for col in X.columns:
    val = float(input(f"Enter {col}: "))
    user_input.append(val)

user_input_scaled = scaler.transform([user_input])
prediction = model.predict(user_input_scaled)

print(f"\nPredicted Property Tax: ${prediction[0]:.2f}")
