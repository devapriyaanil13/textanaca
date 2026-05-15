import streamlit as st
import pickle
import re

model = pickle.load(open("model.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

st.title("Movie Review Sentiment Analysis")

review = st.text_area("Enter your review")

if st.button("Predict"):
    cleaned_review = clean_text(review)
    prediction = model.predict([cleaned_review])[0]

    if prediction == "positive":
        st.success("Positive Review ")
    else:
        st.error("Negative Review ")