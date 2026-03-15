import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = {"employee_id": [1, 2, 3, 4, 5],
    "employee_name": ["Amit", "Priya", "Rahul", "Sneha", "Vikram"],
    "age": [25, None, 40, 35, None],   # some nulls for imputation
    "salary": [50000, 60000, 55000, 70000, 80000],
    "experience": [2, 5, 7, 10, 12],
    "department": ["HR", "IT", "Finance", "IT", "HR"],
    "gender": ["Male", "male", "M", "Female", "F"],
    "city": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata"]
}

df = pd.DataFrame(data)

# i. Load dataset and display
print(f"employee data:\n{df}")

# ii. Null values in age column and impute with mean
null_values=df['age'].isnull().sum()
print(f"null values in age column={null_values}")
df["age"] = df["age"].fillna(df["age"].mean())
print(f"age column after imputation:\n{df['age']}")

# iii. Unique department names
print(f"unique departments:\n{df['department'].unique()}")

# iv. Make gender column consistent
df["gender"] = df["gender"].replace(["male","M"],"Male")
df["gender"] = df["gender"].replace(["female","F"],"Female")
print(f"gender column after cleaning:\n{df['gender']}")

# v. Plot line graphs
plt.plot(df["experience"], df["salary"])
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

plt.plot(df["experience"], df["age"])
plt.title("Age vs Experience")
plt.xlabel("Experience")
plt.ylabel("Age")
plt.show()

# vi. Normalize age, salary, experience
scaler = MinMaxScaler()
df[["age","salary","experience"]] = scaler.fit_transform(df[["age","salary","experience"]])
print(f"normalized data:\n{df[['age','salary','experience']]}")

# vii. Remove outliers from salary using IQR
q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3-q1
l = q1-1.5*iqr
u = q3+1.5*iqr

outliers = df[(df["salary"] < l) | (df["salary"] > u)]
print(f"outliers in salary column:\n{outliers}")

new_df = df[(df["salary"] >= l) & (df["salary"] <= u)]
print(f"data without outliers:\n{new_df}")
