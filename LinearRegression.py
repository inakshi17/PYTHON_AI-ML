import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('salary_prediction.csv')
X = df[['years_of_experience']] # Input (must be 2D)
y = df['salary']               # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Slope (Coefficient): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

plt.scatter(X, y, color='blue', label='Actual Data') # Scatter plot for points
plt.plot(X, model.predict(X), color='red', label='Best Fit Line') # Line plot
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

new_data = [[5], [10], [15]] # Predicting for 5, 10, and 15 years
predictions = model.predict(new_data)
print(f"Predictions for 5, 10, 15 years: {predictions}")

y_pred = model.predict(X_test)
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"R-squared Score: {r2_score(y_test, y_pred):.2f}")
