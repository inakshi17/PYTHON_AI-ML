import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    "Hours_Studied": [1, 2, 3, 5, 6, 8, 10, 11, 12, 15],
    "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
print("Exam Dataset:")
print(df)

X = df[["Hours_Studied"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

test_hours = np.array([[7]])
prediction = model.predict(test_hours)
probability = model.predict_proba(test_hours)

print(f"\nPrediction for 7 hours: {'Passed' if prediction[0] == 1 else 'Failed'}")
print(f"Probability of passing: {probability[0][1]*100:.2f}%")
