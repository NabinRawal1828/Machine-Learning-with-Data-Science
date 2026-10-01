import streamlit as st
import joblib
#load the model
model = joblib.load("model.pkl")
st.number_input("Age:")
st.number_input("Experience")