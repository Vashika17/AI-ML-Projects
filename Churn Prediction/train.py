import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from preprocess import load_data, preprocess
from evaluate import evaluate

data = load_data("data/churn.csv")
data = preprocess(data)

X = data.drop("churn", axis=1)
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

evaluate(model, X_test, y_test)

pickle.dump(model, open("models/model.pkl", "wb"))
