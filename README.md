⚡ EV Smart Analytics & Assistance System

A smart EV analytics web platform built with Streamlit, integrating:

📊 EV performance & charging analytics

🤖 AI-powered EV assistant chatbot

🧠 Machine learning-based prediction engine

Designed for EV owners, researchers, and developers to explore real-world EV behavior and make informed decisions.

🚀 Project Overview

This system enables you to:

Analyze EV dataset patterns (range, battery, charging)

Visualize usage & efficiency metrics

Predict EV performance using ML

Ask EV-related questions to an intelligent chatbot

Explore a clean & interactive Streamlit dashboard

🎯 Key Features

✅ EV Performance & Battery Analytics
✅ Charging Behavior & Cost Analysis
✅ Trip & Efficiency Visualization
✅ Machine Learning-Driven EV Metrics Prediction
✅ AI Assistant powered by OpenAI API
✅ Modern & responsive Streamlit UI

🧠 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
ML	Scikit-Learn, Pandas, NumPy
Visuals	Plotly, Matplotlib, Seaborn
Chatbot	OpenAI API
Version Control	Git + GitHub


📁 Project Structure

EV-Smart-Analytics-Assistance-System/
│
├── app.py                     # Streamlit main dashboard
├── chatbot.py                 # AI chatbot integration
├── train_model.py             # Model training script
│
├── data/                      # Datasets (local CSV files)
│   ├── ev_data.csv
│   ├── trip_logs.csv
│   ├── chatbot_data.csv
│   └── charging_data.csv   (not stored on GitHub)
│
├── models/                   
│   ├── model.pkl
│   └── scaler.pkl
│
├── utils/
│   ├── preprocessing.py
│   └── visualizations.py
│
├── requirements.txt
└── README.md


📂 Dataset Access

⚠️ The charging dataset (~115MB) exceeded GitHub's file limit, so it is hosted externally.

📥 Download Dataset:
https://drive.google.com/file/d/1uKnYeaDew3ih_Tk45mEccpM6amg6ldiZ/view?usp=sharing

After download, place inside:

data/charging_data.csv

📊 Dataset Information
File	Description
ev_data.csv	Vehicle model, battery capacity, manufacturer, range
charging_data.csv	Charging duration, power, session logs, cost
trip_logs.csv	Distance, speed, energy usage
chatbot_data.csv	Custom data for chatbot fine-tuning

Sources: Kaggle, Data.gov, synthetic EV dataset

⚙️ Setup & Installation
Clone repo:
git clone https://github.com/mahendramanikanta/EV-Smart-Analytics-Assistance-System.git
cd EV-Smart-Analytics-Assistance-System

Install dependencies:
pip install -r requirements.txt

Run Streamlit dashboard:
streamlit run app.py

🤖 AI Chatbot Setup

Replace YOUR_API_KEY with your OpenAI API key in chatbot.py

import openai
openai.api_key = "YOUR_API_KEY"


Example usage:

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Best EV under ₹20 lakhs?"}]
)
print(response["choices"][0]["message"]["content"])

🧠 Machine Learning Model

Trains on EV dataset (battery, range, energy)

Saves model & scaler in /models/

Script: train_model.py

Future enhancements:

Neural networks for range prediction

Real-time model update from user data

🧩 Planned Enhancements
Feature	Status
Streamlit Dashboard UI	✅ Done
Dataset Cleaning & EDA	✅ Done
EV ML Model	✅ Done
Chatbot Integration	🛠 In progress
Streamlit Cloud Deployment	⏳ Next
Voice-based EV Assistant	Coming
IoT sensor stream input	Coming
👤 Author

Manikanta
🎓 CSE (IoT) | AI & IoT Enthusiast

🌐 GitHub: https://github.com/mahendramanikanta

🔗 LinkedIn: https://www.linkedin.com/in/pathakotimanikanta

📜 License

MIT License — Free to use for learning & research 🧠✨
