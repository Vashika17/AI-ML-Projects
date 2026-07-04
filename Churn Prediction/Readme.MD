# Customer Churn Prediction (ML Classification)

Predicts whether a telecom customer will churn (leave) based on their account
and usage attributes — a classic supervised classification problem.

## What it does
1. **Data quality checks** — missing values, duplicates
2. **EDA** — churn rate, average tenure/charges split by churn status
3. **Feature engineering** — encodes categorical columns (contract type,
   internet service, tech support, etc.) into numbers models can use
4. **Model training** — trains Random Forest and Gradient Boosting,
   tuned with `GridSearchCV`
5. **Evaluation** — compares both models by ROC-AUC, picks the better one,
   prints a full classification report
6. **Visualization** — feature importance chart + confusion matrix

## How to run
```bash
pip install pandas scikit-learn matplotlib
python generate_data.py   # creates customer_churn.csv
python train_model.py     # trains models, prints metrics, saves charts
```

## Files
- `generate_data.py` — creates a synthetic but realistic telecom churn dataset
- `train_model.py` — the ML pipeline: load → EDA → encode → train → evaluate → visualize
- `customer_churn.csv` — the dataset (800 customers)
- `charts/feature_importance.png`, `charts/confusion_matrix.png`

