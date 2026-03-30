import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dataset = {
    "age": [10, 14, 17, 20, 30, 35, 40, 45], # Added a few more points for better training
    "weight": [45, 32, 23, 28, 25, 22, 20, 18]
}

df = pd.DataFrame(dataset)

X = df[["age"]]
y = df[["weight"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

age_to_predict = np.array([[25]])
prediction = model.predict(age_to_predict)

print(f"Dataframe:\n{df}\n")
print(f"Predicted weight for age 25: {prediction[0][0]:.2f} kg")

print(f"Model Accuracy (R^2 Score): {model.score(X_test, y_test):.2f}")
