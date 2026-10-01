from pathlib import Path

import streamlit as st
import joblib
#load the model
model = joblib.load(Path(__file__).with_name('logistic_model.pkl'))
st.title('Logistic Regression Model')
st.write('This is a simple logistic regression model.')
age = st.number_input('Enter the age', min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")

if st.button('Predict'):
	prediction = model.predict([[age]])[0]

	if prediction == 1:
		st.success('The customer will purchase the product.')
	else:
		st.info('The customer will not purchase the product.')


