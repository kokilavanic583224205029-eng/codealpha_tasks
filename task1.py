# iris_classification_knn.py
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import joblib

# 1) Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 2) (Optional) Save dataset to CSV
df.to_csv("iris_dataset.csv", index=False)
print("Saved iris_dataset.csv")

# 3) Split into train/test
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4) Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5) Train KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# 6) Evaluate
y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print(f"\nModel accuracy: {accuracy:.4f}\n")
print("Confusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)

# 7) Save model and scaler for later use
joblib.dump(knn, "knn_iris_model.joblib")
joblib.dump(scaler, "iris_scaler.joblib")
print("Saved knn_iris_model.joblib and iris_scaler.joblib")

# 8) Plot pairwise scatter matrix and save
axes = scatter_matrix(df.iloc[:, :4], diagonal='kde', figsize=(10, 10))
# re-plot points per species to visually separate them (no custom colors set)
for i, ax_row in enumerate(axes):
    for j, ax in enumerate(ax_row):
        if i != j:
            for species_name in iris.target_names:
                mask = df['species'] == species_name
                ax.scatter(df.loc[mask, df.columns[j]], df.loc[mask, df.columns[i]], s=20)
plt.suptitle("Iris pairwise scatter matrix (features)")
plt.savefig("iris_scatter_matrix.png", bbox_inches='tight')
plt.close()
print("Saved iris_scatter_matrix.png")
