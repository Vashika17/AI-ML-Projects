## Customer Churn Prediction using Machine Learning

## 🚀 Overview

This project focuses on predicting customer churn in a telecom dataset using supervised machine learning techniques.
The goal is to identify customers who are likely to leave the service, enabling businesses to take proactive retention actions.

---

## 📁 Dataset Description

* Dataset: Telecom Customer Churn Dataset

* Total Records: ~7000 customers

* Features: 20+ attributes including:

  * Customer demographics (gender, senior citizen)
  * Account information (tenure, contract type)
  * Services subscribed (internet, phone, streaming)
  * Billing details (monthly charges, total charges)

* Target Variable:

  * `Churn` → Yes (1) / No (0)

---

## ⚙️ Data Preprocessing

* Handled missing values
* Converted categorical variables using one-hot encoding
* Feature selection and transformation
* Train-test split (80-20)

---

## 🧠 Model Used

* Random Forest Classifier
* Also experimented with:

  * Logistic Regression
  * Gradient Boosting

---

## 📈 Evaluation Metrics

* Accuracy: ~85%+
* ROC-AUC Score: ~0.91
* Confusion Matrix for performance visualization

---

## 📊 Key Insights

* Customers with higher monthly charges are more likely to churn
* Long-term contract users show lower churn rates
* Certain service combinations increase churn probability

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/train.py
```

---

## 📸 Output Visualization

(Add your screenshots here)

* Confusion Matrix
* Feature Importance Graph
* ROC Curve

Example:
![Confusion Matrix](images/confusion_matrix.png)

---

## 📂 Project Structure

```
churn-prediction/
│── data/
│── src/
│── models/
│── notebooks/
│── README.md
```

---

## 💡 Learnings

* Built an end-to-end ML pipeline from data preprocessing to model evaluation
* Understood feature importance and business impact of predictions
* Learned how to interpret classification metrics in real-world scenarios

---

## 🚀 Future Improvements

* Hyperparameter tuning with GridSearchCV
* Deploy as a web application
* Integrate real-time prediction API

