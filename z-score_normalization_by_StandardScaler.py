import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Hours_Studied": [1, 2, 3, 5, 6, 8, 10, 11, 12, 15]
}
df = pd.DataFrame(data)

scaler = StandardScaler()

df['Hours_Scaled'] = scaler.fit_transform(df[['Hours_Studied']])

print("Original vs Normalized Data:")
print(df)

print(f"\nNew Mean: {df['Hours_Scaled'].mean():.2f}")
print(f"New Std Dev: {df['Hours_Scaled'].std():.2f}")
