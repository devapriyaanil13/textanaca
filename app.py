import streamlit as st
import pickle
model = pickle.load(open("model.pkl", "rb"))
st.title("CA2 Sentiment Analysis")
review = st.text_area("Enter Movie Review")
if st.button("Predict"):
    prediction = model.predict([review])
    st.success(f"Sentiment : {prediction[0]}")