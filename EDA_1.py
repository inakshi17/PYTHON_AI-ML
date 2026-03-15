import pandas as pd
data1={"appointment_id": [1, 2, 3, 4, 5],
    "patient_id": [101, 102, 103, 104, 105],
    "appointment_date": ["2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14"],
    "consultation_fee": [500, 700, 600, 800, 550],
    "diagnosis": ["Flu", "Diabetes", "Hypertension", "Asthma", "Flu"],
    "bp": ["Normal", "130/90", "140/95", "Normal", "120/80"]
}
data2={"patient_id": [101, 102, 103, 104, 105],
    "patient_name": ["Amit", "Priya", "Rahul", "Sneha", "Vikram"],
    "age": [-25, 45, 60, 30, 50], 
    "gender": ["Male", "Female", "Male", "Female", "Male"],
    "city": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata"],
    "cholesterol": [None, 210, 190, None, 220]  
}


# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Save to CSV
df1.to_csv("appointments.csv", index=False)
df2.to_csv("patient_info.csv", index=False)

# Read 
df1 = pd.read_csv("appointments.csv")
df2 = pd.read_csv("patient_info.csv")

print(f"appointments data:\n{df1}")
print(f"patient info data:\n{df2}")

# Merge datasets
df = pd.merge(df1, df2, on="patient_id", how="inner")
print(f"merged data:\n{df}")

# Convert negative ages to absolute
df["age"] = abs(df["age"])
print(f"age column after abs:\n{df['age']}")

# Remove outliers
q1 = df["age"].quantile(0.25)
q3 = df["age"].quantile(0.75)
iqr = q3-q1
l = q1-1.5*iqr
u = q3+1.5*iqr

outliers = df[(df["age"] < l) | (df["age"] > u)]
print(f"outliers in age column:\n{outliers}")

new_df = df[(df["age"] >= l) & (df["age"] <= u)]
print(f"data without outliers:\n{new_df}")

# Replace "Normal" in bp column
df["bp"] = df["bp"].replace("Normal", "120/80")
print(f"new bp data:\n{df['bp']}")

# Impute null cholesterol values with mean
df["cholesterol"] = df["cholesterol"].fillna(df["cholesterol"].mean())
print(f"cholesterol column after imputation:\n{df['cholesterol']}")

# Group by gender and calculate average consultation fee
avg = df.groupby("gender")["consultation_fee"].mean()
print(f"average consultation fee by gender:\n{avg}")
