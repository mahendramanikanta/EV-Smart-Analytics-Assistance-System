⚡ EV Smart Analytics & Assistance System

An intelligent Streamlit-based dashboard that integrates Electric Vehicle (EV) data analytics, ML predictions, and an AI-powered chatbot for smarter decision-making and real-time EV insights.

🚀 Project Overview

The EV Smart Analytics & Assistance System enables EV owners, analysts, and researchers to:

Analyze and visualize EV performance trends

Predict energy usage and range using ML models

Interact with an integrated AI chatbot for EV-related assistance

🎯 Key Features

✅ EV Data Analysis – View detailed insights about vehicle performance and battery metrics.
✅ Charging Behavior Insights – Explore patterns in charging sessions, energy costs, and time usage.
✅ Trip Analytics – Visualize distance, efficiency, and power consumption trends.
✅ Machine Learning Predictions – Predict range or battery degradation using trained ML models.
✅ AI Chatbot Integration – Ask EV-related questions and get intelligent, data-backed responses.
✅ Modern Streamlit UI – Built with a clean dark theme and dynamic navigation.

🧠 Technologies Used
Component	Technology
Frontend	Streamlit
Backend	Python
ML Model	Scikit-learn, Pandas, NumPy
Visualization	Matplotlib, Seaborn, Plotly
Chatbot	OpenAI API
Dataset Handling	Pandas, CSV
Version Control	Git + GitHub
📁 Folder Structure
EV Smart Analytics & Assistance System/
│
├── app.py                     # Main Streamlit app
├── chatbot.py                 # Chatbot API integration
├── model_training.py          # Model building and training
├── train_model.py             # Model testing / retraining
│
├── data/                      # Datasets
│   ├── ev_data.csv
│   ├── charging_data.csv
│   ├── trip_logs.csv
│   ├── chatbot_data.csv
│
├── models/                    # Trained ML models
│   ├── model.pkl
│   └── scaler.pkl
│
├── utils/                     # Helper scripts
│   ├── preprocessing.py
│   └── visualizations.py
│
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation

📊 Dataset Description

The project uses multiple CSV files covering EV specifications, trip data, and charging patterns.

Dataset	Description
ev_data.csv	Vehicle model, battery capacity, manufacturer, range
charging_data.csv	Charging duration, power, cost, and session logs
trip_logs.csv	Trip distance, average speed, and energy usage
chatbot_data.csv	Reference data for EV chatbot responses

Sources: Kaggle Datasets, Data.gov, and synthetic test data

⚙️ Installation

Clone the repository

git clone https://github.com/mahendramanikanta/EV-Smart-Analytics.git
cd EV-Smart-Analytics


Install dependencies

pip install -r requirements.txt


Run Streamlit app

streamlit run app.py


Open in browser

http://localhost:8501

🤖 Chatbot Integration

The chatbot is powered by the OpenAI API and answers EV-related queries intelligently.

Example:

import openai

openai.api_key = "YOUR_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Which EV offers the best range under ₹20 lakh?"}
    ]
)

print(response["choices"][0]["message"]["content"])

🧩 Machine Learning Model

Training Script: model_training.py

Testing Script: train_model.py

Saved Models: models/model.pkl, models/scaler.pkl

The model predicts metrics such as range, efficiency, or energy consumption based on historical data.

📈 Future Enhancements

🌐 Real-time EV API data (Tesla, Tata EV, MG)

🎙️ Voice-enabled chatbot assistant

🛰️ Route optimization using charging station data

🔋 Predictive maintenance and fault detection via IoT sensors

👤 Author

Manikanta
🎓 Engineering Student – CSE (IoT)
💡 Passionate about AI, IoT, and Smart Systems

🔗 GitHub: mahendramanikanta

🔗 LinkedIn: pathakotimanikanta

📜 License

This project is licensed under the MIT License – feel free to modify and use for educational or research purposes.