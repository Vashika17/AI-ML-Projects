"""
train_model.py
---------------
End-to-end ML pipeline for customer churn prediction:

  1. Load data + data quality checks (missing values, duplicates)
  2. EDA (churn rate, correlations)
  3. Feature engineering (encode categorical variables)
  4. Train/test split
  5. Train Random Forest + Gradient Boosting, tune with GridSearchCV
  6. Evaluate with ROC-AUC
  7. Visualize: feature importance + confusion matrix

Run: python train_model.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.preprocessing import LabelEncoder

CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

# ------------------------------------------------------------------
# 1. LOAD + DATA QUALITY CHECKS
# ------------------------------------------------------------------
df = pd.read_csv("customer_churn.csv")

print("Shape:", df.shape)
print("\nMissing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nChurn distribution:\n", df["churn"].value_counts(normalize=True))

# ------------------------------------------------------------------
# 2. EDA (quick look)
# ------------------------------------------------------------------
print("\nAverage tenure by churn status:\n", df.groupby("churn")["tenure_months"].mean())
print("\nAverage monthly charges by churn status:\n", df.groupby("churn")["monthly_charges"].mean())

# ------------------------------------------------------------------
# 3. FEATURE ENGINEERING: encode categorical columns
# ------------------------------------------------------------------
categorical_cols = ["contract", "internet_service", "tech_support", "online_security",
                     "paperless_billing", "payment_method"]

df_encoded = df.copy()
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    encoders[col] = le

target_le = LabelEncoder()
df_encoded["churn"] = target_le.fit_transform(df_encoded["churn"])  # Yes=1, No=0 (check order)

feature_cols = ["senior_citizen", "tenure_months", "contract", "internet_service",
                 "tech_support", "online_security", "paperless_billing",
                 "payment_method", "monthly_charges", "total_charges"]

X = df_encoded[feature_cols]
y = df_encoded["churn"]

# ------------------------------------------------------------------
# 4. TRAIN/TEST SPLIT
# ------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------------
# 5. TRAIN MODELS + GRIDSEARCHCV
# ------------------------------------------------------------------
rf_param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10, None],
}
rf_grid = GridSearchCV(RandomForestClassifier(random_state=42), rf_param_grid, cv=3, scoring="roc_auc")
rf_grid.fit(X_train, y_train)
best_rf = rf_grid.best_estimator_
print("\nBest Random Forest params:", rf_grid.best_params_)

gb_param_grid = {
    "n_estimators": [100, 200],
    "learning_rate": [0.05, 0.1],
}
gb_grid = GridSearchCV(GradientBoostingClassifier(random_state=42), gb_param_grid, cv=3, scoring="roc_auc")
gb_grid.fit(X_train, y_train)
best_gb = gb_grid.best_estimator_
print("Best Gradient Boosting params:", gb_grid.best_params_)

# ------------------------------------------------------------------
# 6. EVALUATE
# ------------------------------------------------------------------
rf_proba = best_rf.predict_proba(X_test)[:, 1]
gb_proba = best_gb.predict_proba(X_test)[:, 1]

rf_auc = roc_auc_score(y_test, rf_proba)
gb_auc = roc_auc_score(y_test, gb_proba)

print(f"\nRandom Forest ROC-AUC: {rf_auc:.3f}")
print(f"Gradient Boosting ROC-AUC: {gb_auc:.3f}")

# pick the better model for the final report
best_model, best_name, best_proba = (best_rf, "Random Forest", rf_proba) if rf_auc >= gb_auc else (best_gb, "Gradient Boosting", gb_proba)
y_pred = best_model.predict(X_test)

print(f"\nUsing {best_name} as final model (higher ROC-AUC)")
print("\nClassification report:\n", classification_report(y_test, y_pred, target_names=target_le.classes_))

# ------------------------------------------------------------------
# 7. VISUALIZE: feature importance + confusion matrix
# ------------------------------------------------------------------
importances = pd.Series(best_model.feature_importances_, index=feature_cols).sort_values(ascending=True)

plt.figure(figsize=(8, 5))
plt.barh(importances.index, importances.values, color="#C0504D")
plt.title(f"Feature Importance ({best_name})")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/feature_importance.png", dpi=120)
plt.close()

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_le.classes_)
disp.plot(cmap="Blues")
plt.title(f"Confusion Matrix ({best_name})")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/confusion_matrix.png", dpi=120)
plt.close()

print(f"\nCharts saved in ./{CHART_DIR}/")