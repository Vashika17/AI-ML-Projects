import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data

def preprocess(data):
    data = data.dropna()
    data = pd.get_dummies(data, drop_first=True)
    return data
