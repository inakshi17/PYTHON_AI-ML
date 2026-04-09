from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = {
    "age": [10, 14, 17, 20, 30, 35, 40, 45],
    "weight": [45, 32, 23, 28, 25, 22, 20, 18]
}
df = pd.DataFrame(dataset)

X = df[["age"]]
y = df["weight"] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsRegressor(n_neighbors=3) 

knn.fit(X_train, y_train)

predictions = knn.predict(X_test)
print(f"Predicted Weights: {predictions}")
print(f"Actual Weights: {y_test.values}")
