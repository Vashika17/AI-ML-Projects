import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("models/model.pkl", "rb"))

st.title("Customer Churn Prediction")

input_data = st.text_input("Enter comma-separated feature values")

if st.button("Predict"):
    values = list(map(float, input_data.split(",")))
    df = pd.DataFrame([values])
    pred = model.predict(df)[0]
    st.write("Churn" if pred == 1 else "No Churn")
