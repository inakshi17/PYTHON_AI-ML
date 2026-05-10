import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

data = {
    'age': np.random.randint(20, 80, 200),
    'bp': np.random.randint(80, 160, 200),
    'cholesterol': np.random.randint(150, 300, 200),
    'sugar': np.random.randint(70, 150, 200),
    'weight': np.random.randint(50, 100, 200),
    'target': np.random.randint(0, 100, 200)
}
df = pd.DataFrame(data)
X = df.drop('target', axis=1)
y = df['target']

sfs_lr_fwd = SFS(LinearRegression(), k_features=3, forward=True)
sfs_knn_fwd = SFS(KNeighborsRegressor(), k_features=3, forward=True)

sfs_lr_fwd.fit(X, y)
sfs_knn_fwd.fit(X, y)

print("Forward - Linear Regression Features:", sfs_lr_fwd.k_feature_names_)
print("Forward - KNN Features:", sfs_knn_fwd.k_feature_names_)

sfs_lr_back = SFS(LinearRegression(), k_features=3, forward=False)
sfs_knn_back = SFS(KNeighborsRegressor(), k_features=3, forward=False)

sfs_lr_back.fit(X, y)
sfs_knn_back.fit(X, y)

print("\nBackward - Linear Regression Features:", sfs_lr_back.k_feature_names_)
print("Backward - KNN Features:", sfs_knn_back.k_feature_names_)

print("\n--- Final Comparison ---")
print("Linear Regression (Fwd vs Back):", sfs_lr_fwd.k_feature_names_, "vs", sfs_lr_back.k_feature_names_)
print("KNN (Fwd vs Back):", sfs_knn_fwd.k_feature_names_, "vs", sfs_knn_back.k_feature_names_)
