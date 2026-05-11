import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

data = {
    'Study_Hours': np.random.randint(10, 50, 5000),
    'Attendance': np.random.randint(60, 100, 5000),
    'Assignment_Score': np.random.randint(0, 100, 5000),
    'Internal_Marks': np.random.normal(50, 15, 5000), 
    'Extracurricular': np.random.choice(['Yes', 'No'], 5000),
    'Final_Result': np.random.choice(['Pass', 'Fail'], 5000)
}
df = pd.DataFrame(data)

le = LabelEncoder()
df['Extracurricular'] = le.fit_transform(df['Extracurricular'])
df['Final_Result'] = le.fit_transform(df['Final_Result'])

Q1 = df['Internal_Marks'].quantile(0.25)
Q3 = df['Internal_Marks'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['Internal_Marks'] >= lower_bound) & (df['Internal_Marks'] <= upper_bound)]

X = df.drop('Final_Result', axis=1)
y = df['Final_Result']
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.30, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
