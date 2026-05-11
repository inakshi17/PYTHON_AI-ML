import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('loan_approval_dataset.csv')

X = df.drop('Loan_Approval', axis=1)
y = df['Loan_Approval']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

dt_model = DecisionTreeClassifier(criterion='entropy', max_depth=5)
dt_model.fit(X_train, y_train)

y_pred = dt_model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(15, 10))
plot_tree(dt_model, feature_names=X.columns, class_names=['Rejected', 'Approved'], filled=True)
plt.show()

new_applicant = [X.iloc[0].values] 
prediction = dt_model.predict(new_applicant)
print(f"Prediction for new applicant: {'Approved' if prediction[0] == 1 else 'Rejected'}")
