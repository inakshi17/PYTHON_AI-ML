import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'patient_id': [1, 2, 3, 4],
    'name': ['Amit', None, 'Esha', 'Daya'],
    'age': [25, -5, 30, 22],
    'gender': ['M', 'F', 'Male', 'F'],
    'city': ['delhi', 'Mumbai', 'DELHI', 'pune']
}
data2 = {
    'patient_id': [1, 2, 3, 4],
    'admission_date': ['2023/01/01', '02-01-2023', '2023.01.03', '04/01/2023'],
    'height_cm': ['170', '160', '175', '155'],
    'bp': ['high', '120/80', 'high', '110/70'],
    'sugar_level': [100, None, 120, 110],
    'visit_cost': [500, 600, 700, 800],
    'diagnosis': ['Flu', 'Cold', 'Flu', 'Fever']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df = pd.merge(df1, df2, on='patient_id', how='inner')

df['name'] = df['name'].fillna("unknown")

df['age'] = df['age'].abs()

df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female'})

df['city'] = df['city'].str.lower()
df['height_cm'] = df['height_cm'].fillna(df['height_cm'].mean())

df['bp'] = df['bp'].replace('high', '140/90')

df['sugar_level'] = df['sugar_level'].fillna(df['sugar_level'].mean())

stats = df.groupby('gender')['visit_cost'].agg(['mean', 'min', 'max'])
print(stats)

plt.hist(df['diagnosis'])
plt.title("Diagnosis Distribution")
plt.show()
