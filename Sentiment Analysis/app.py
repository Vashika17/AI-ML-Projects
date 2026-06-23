import streamlit as st
import pickle
from preprocess import clean_text

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Sentiment Analysis App")

text = st.text_area("Enter text")

if st.button("Predict"):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)[0]
    st.write("Prediction:", pred)
