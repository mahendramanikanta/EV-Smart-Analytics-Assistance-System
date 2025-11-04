# app.py
import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from chatbot import chatbot_response

# Load model and scaler
model = pickle.load(open('models/model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

st.title("🚗 Electric Vehicle Data Analysis & Prediction Dashboard")

menu = ["Home", "Data Visualization", "Predict Range", "Chatbot"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.write("### Welcome to the EV Dashboard")
    st.write("Explore EV data, visualize insights, predict electric range, and chat with the EV Bot!")

elif choice == "Data Visualization":
    st.subheader("Electric Range Distribution")
    ev_data = pd.read_csv("data/ev_data.csv")
    sns.histplot(ev_data['Electric Range'], kde=True)
    st.pyplot(plt)

elif choice == "Predict Range":
    st.subheader("🔮 Predict Electric Range")
    year = st.number_input("Model Year", min_value=1995, max_value=2025, step=1)
    msrp = st.number_input("Base MSRP ($)", min_value=10000, max_value=200000, step=1000)

    if st.button("Predict"):
        scaled = scaler.transform([[year, msrp]])
        prediction = model.predict(scaled)
        st.success(f"Estimated Electric Range: {prediction[0]:.2f} miles")

elif choice == "Chatbot":
    st.subheader("💬 Chat with EV Assistant")
    user_input = st.text_input("You: ", "")
    if st.button("Send"):
        st.write("Bot:", chatbot_response(user_input))
