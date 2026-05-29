import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score, confusion_matrix

try:
    df = pd.read_csv('credit_risk.csv')
except FileNotFoundError:
    import numpy as np
    data = {
        'Age': np.random.randint(18, 70, 100),
        'Credit_Score': np.random.randint(300, 850, 100),
        'Monthly_Income': np.random.randint(2000, 15000, 100),
        'Existing_Loans': np.random.randint(0, 5, 100),
        'Risk_Level': np.random.choice(['Low', 'High'], 100)
    }
    df = pd.DataFrame(data)

le = LabelEncoder()
df['Risk_Level'] = le.fit_transform(df['Risk_Level'])

X = df.drop('Risk_Level', axis=1)
y = df['Risk_Level']
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

k_values = [3, 5, 7]
accuracies = []

best_k = 3
max_acc = 0

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)
    print(f"Accuracy for K={k}: {acc:.2f}")
    
    if acc > max_acc:
        max_acc = acc
        best_k = k

print(f"\nDisplaying Confusion Matrix for Best K={best_k}")
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train, y_train)
y_pred_best = best_knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred_best)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title(f"Confusion Matrix (K={best_k})")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
plt.figure(figsize=(6, 4))
plt.plot(k_values, accuracies, marker='o', linestyle='--', color='green')
plt.title("K-Value vs. Accuracy")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Accuracy Score")
plt.xticks(k_values)
plt.grid(True)
plt.show()
