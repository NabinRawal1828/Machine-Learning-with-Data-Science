import streamlit as st 
import joblib
import pandas as pd
# load the model
model = joblib.load('model.pkl')
st.title("Placement Prediction")
st.write("Predict the placement outcome of a student based on their CGPA and ScoreBias.")
cgpa = st.number_input("Enter CGPA",format="%.0f", min_value=0.0, max_value=10.0, step=0.01)
score_bias = st.number_input("Enter ScoreBias",format="%.0f", min_value=0.0, max_value=100.0, step=0.01)

if st.button("Predict"):
    input_data = pd.DataFrame([[cgpa, score_bias]], columns=['CGPA', 'ScoreBias'],formatters={'CGPA': '{:.0f}', 'ScoreBias': '{:.0f}'})
    prediction = model.predict(input_data)
    st.write(f"The predicted placement outcome is: {prediction[0]}")
    
# if prediction[0] == 1:
#     st.success("The student is likely to be placed.")
# else:
#     st.error("The student is unlikely to be placed.")
