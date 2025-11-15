# ⚡ EV Smart Analytics & Assistance System

A smart Electric Vehicle (EV) analytics platform built using **Streamlit**, integrating:

* 📊 EV performance & charging analytics
* 🤖 AI-powered Gemini EV assistant chatbot
* 🧠 Machine learning–based EV range prediction
* 🎨 Modern UI with visualizations & metrics

Built for **EV owners, researchers, developers, and data analysts** to explore, visualize, and understand EV behavior.

---

# 🚀 Project Overview

This dashboard allows you to:

* Analyze EV dataset patterns (range, battery, model year)
* Visualize efficiency and usage statistics
* Predict EV range using an ML model
* Interact with an **AI EV Assistant Chatbot** (Gemini-powered)
* Explore EV insights through an interactive Streamlit UI

---

# 🎯 Key Features

### 🔍 EV Data & Performance Analytics

* Range distribution
* Manufacturer statistics
* Range vs model year
* State-wide EV counts

### 🔮 Machine Learning Range Predictor

* Predict EV electric range
* Uses Linear Regression + StandardScaler
* Model stored as `models/model.pkl`

### 🤖 Intelligent EV Chatbot (Gemini API)

* Uses Google’s **Gemini-Pro** model
* Works even without API key (rule-based fallback)
* Loaded securely using **secrets.toml**

### 🎨 Modern UI

* Dark theme
* Clean layout
* KPI metrics
* Professional charts (Seaborn + Matplotlib)

---

# 🧠 Tech Stack

| Component       | Technology                  |
| --------------- | --------------------------- |
| Frontend        | Streamlit                   |
| Backend         | Python                      |
| ML Model        | Scikit-Learn                |
| Data Handling   | Pandas                      |
| Visualization   | Seaborn, Matplotlib, Plotly |
| Chatbot         | Google Gemini API           |
| Deployment      | Streamlit Cloud             |
| Version Control | Git + GitHub                |

---

# 📁 Project Structure (Updated)

```
EV-Smart-Analytics-Assistance-System/
│
├── app.py                     # Main dashboard with multipage UI
├── chatbot.py                 # Gemini chatbot + rule-based fallback
├── train_model.py             # ML model training script
│
├── data/
│   ├── ev_data.csv
│   ├── trip_logs.csv
│   ├── chatbot_data.csv
│   └── charging_data.csv (Not uploaded — stored in Google Drive)
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── utils/
│   ├── preprocessing.py
│   └── visualizations.py
│
├── .streamlit/
│   └── secrets.toml           # Contains GEMINI_API_KEY securely
│
├── requirements.txt
└── README.md
```

---

# 📂 Dataset Access (Updated)

⚠️ *Large file `charging_data.csv` (~115 MB) cannot be uploaded to GitHub (100MB limit).*

So it has been moved to Google Drive:

📥 **Download charging_data.csv:**
👉 [https://drive.google.com/file/d/1uKnYeaDew3ih_Tk45mEccpM6amg6ldiZ/view?usp=sharing](https://drive.google.com/file/d/1uKnYeaDew3ih_Tk45mEccpM6amg6ldiZ/view?usp=sharing)

After downloading, place here:

```
data/charging_data.csv
```

---

# 📊 Dataset Information

| File              | Description                           |
| ----------------- | ------------------------------------- |
| ev_data.csv       | Model, battery, price, electric range |
| charging_data.csv | Charging sessions, power, cost        |
| trip_logs.csv     | Distance, speed, energy efficiency    |
| chatbot_data.csv  | Training info for EV chatbot          |

---

# ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mahendramanikanta/EV-Smart-Analytics-Assistance-System.git
cd EV-Smart-Analytics-Assistance-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Gemini API Key

Create this file:

```
.streamlit/secrets.toml
```

Paste:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

# 🤖 AI Chatbot (Updated)

Uses **Gemini-Pro** by default:

```python
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")
```

Fallback rule-based chatbot activates **if API key is missing or fails**.

---

# 🧠 ML Model Pipeline (Updated)

### ✔ Training Script Updated

`train_model.py` now:

* Loads EV dataset
* Cleans columns
* Trains Linear Regression model
* Scales features
* Saves `model.pkl` & `scaler.pkl`

### ✔ Prediction in UI

`app.py` auto-detects missing model files & warns the user.

---

# 🧩 Recent Additions (What We Added 🔥)

### ✅ Upgraded `app.py`

* Full navigation system
* Error handling
* API key loader
* Safe CSV loader
* EV Metrics section
* Professional UI components

### ✅ Upgraded `chatbot.py`

* Full Gemini integration
* Rule-based fallback
* Exception handling
* Cleaner response formatting

### ✅ Added `.streamlit/secrets.toml` support

* Secure API key handling
* No keys inside source code

### ✅ Improved Folder Structure

* Cleaner, modular, professional repository

### ✅ Deployment-ready Architecture

* Works with Streamlit Cloud
* Works with localhost
* No path errors

---

# 🧩 Planned Enhancements

| Feature                        | Status        |
| ------------------------------ | ------------- |
| UI Enhancement                 | 🔜            |
| Voice-based chatbot            | Coming soon   |
| Lottie animations              | Coming        |
| Streamlit Cloud deployment     | Next step     |
| Realtime EV API data           | Planned       |
| Geolocation-based charging map | Future update |

---

# 👤 Author

**Manikanta**
CSE – IoT | AI • ML • Smart Systems

🌐 GitHub: [https://github.com/mahendramanikanta](https://github.com/mahendramanikanta)
🔗 LinkedIn: [https://www.linkedin.com/in/pathakotimanikanta](https://www.linkedin.com/in/pathakotimanikanta)

---

# 📜 License

MIT License — Free for educational & research use.

---
