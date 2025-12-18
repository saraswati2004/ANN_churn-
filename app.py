import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("ANN_model.h5", compile=False)




st.set_page_config(page_title="Churn Prediction App")

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details below to predict whether they will churn.")

# ---- Input fields ----
credit_score = st.number_input("Credit Score", min_value=0, max_value=1000, value=600)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=3)
balance = st.number_input("Account Balance", min_value=0.0, value=50000.0)
num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_credit_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

# ---- Convert inputs ----
gender = 1 if gender == "Female" else 0

geo_fr = 1 if geography == "France" else 0
geo_es = 1 if geography == "Spain" else 0
geo_ge = 1 if geography == "Germany" else 0

has_credit_card = 1 if has_credit_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0

# Prepare input in correct order
input_data = np.array([[
    credit_score,
    gender,
    age,
    tenure,
    balance,
    num_products,
    has_credit_card,
    is_active_member,
    estimated_salary,
    
    geo_es,
    geo_ge
]])

# ---- Prediction ----
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ The customer is **likely to churn**.")
    else:
        st.success("✅ The customer is **not likely to churn**.")

