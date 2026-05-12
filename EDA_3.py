import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'student_id': [1, 2, 3, 4, 5, 6],
    'student_name': ['Amit', 'Bina', 'Amit', 'Daya', 'Esha', 'Fani'],
    'age': [20, 21, 19, 22, 20, 50], 
    'height': [150, 160, 155, 165, 300, 158], 
    'weight': [50, 60, 55, 65, 58, 200],
    'semester': [1, 2, 1, 3, 2, 4],
    'gender': ['M', 'F', 'M', 'M', 'F', 'M'],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)

print("Shape:", df.shape)

print("Columns:", df.columns.tolist())

print("Null values:\n", df.isnull().sum())

print("Unique Names:", df['student_name'].unique())

plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.plot(df['height'], df['weight'])
plt.title("Height vs Weight")

plt.subplot(1, 3, 2)
plt.plot(df['height'], df['age'])
plt.title("Height vs Age")

plt.subplot(1, 3, 3)
plt.plot(df['weight'], df['age'])
plt.title("Weight vs Age")
plt.show()

plt.scatter(df.index, df['height'])
plt.title("Height Outliers")
plt.show()

df.boxplot()
plt.title("Boxplot for Outliers")
plt.show()

Q1 = df['height'].quantile(0.25)
Q3 = df['height'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['height'] >= lower) & (df['height'] <= upper)]
print("Shape after IQR (Height):", df.shape)

mean = df['weight'].mean()
std = df['weight'].std()
df = df[((df['weight'] - mean) / std).abs() < 3]
print("Shape after Z-score (Weight):", df.shape)
