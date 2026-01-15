import streamlit as st 
import pickle

st.set_page_config(page_title="Income Predictor", page_icon="💰")

st.title("Income Predictor for Employees")
st.caption("This project is built for the AI15 and DS14")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


input = st.number_input(label="Enter years of Experience", min_value=0.0, max_value=10.0, value=1.5, step=0.1)

if st.button("Predict"):
    predictions = model.predict([[input]])[0]
    st.success(predictions)