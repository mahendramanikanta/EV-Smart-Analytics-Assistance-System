# app.py
import os
import pickle
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from chatbot import chat_reply   # <-- now uses Gemini

st.set_page_config(page_title="EV Smart Analytics", page_icon="🔋", layout="wide")
sns.set_style("darkgrid")

# ------------------------------
# Load model + scaler
# ------------------------------
@st.cache_resource
def load_models():
    try:
        model = pickle.load(open("models/model.pkl", "rb"))
        scaler = pickle.load(open("models/scaler.pkl", "rb"))
        return model, scaler, None
    except Exception as e:
        return None, None, str(e)

def safe_load_csv(path):
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()
        return df
    except:
        return None

model, scaler, model_err = load_models()

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title("⚡ EV Smart Analytics")
page = st.sidebar.radio("", ["Home", "Data Visualization", "Predict Range", "Chatbot", "About"])

# Gemini API key (optional)
st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Gemini API Key (optional)")
gemini_api = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Fetch key safely
def get_api_key():
    if gemini_api:
        return gemini_api
    try:
        return st.secrets["GEMINI_API_KEY"]
    except:
        return None

# ------------------------------
# HOME
# ------------------------------
if page == "Home":
    st.title("⚡ EV Smart Analytics & Assistance System")

    st.markdown("""
        A Streamlit dashboard for EV data analysis, ML predictions, and an intelligent chatbot powered by Google Gemini.
    """)

    ev_df = safe_load_csv("data/ev_data.csv")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Records", f"{len(ev_df):,}" if ev_df is not None else "N/A")

    with c2:
        st.metric("Unique Makes",
                  ev_df["Make"].nunique() if (ev_df is not None and "Make" in ev_df.columns) else "N/A")

    with c3:
        st.metric("Max Range",
                  int(ev_df["Electric Range"].dropna().max()) if (ev_df is not None and "Electric Range" in ev_df.columns)
                  else "N/A")

    st.info("Note: Large files like `charging_data.csv` should be stored on Google Drive.")

# ------------------------------
# DATA VISUALIZATION
# ------------------------------
elif page == "Data Visualization":
    st.title("📊 Data Visualization")

    df = safe_load_csv("data/ev_data.csv")
    if df is None:
        st.error("`ev_data.csv` missing. Place it in /data folder.")
        st.stop()

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # --- Range Distribution
    if "Electric Range" in df.columns:
        st.subheader("Electric Range Distribution")
        fig, ax = plt.subplots(figsize=(8,4))
        sns.histplot(df["Electric Range"].dropna(), kde=True, ax=ax)
        st.pyplot(fig)

    # --- Top 10 Manufacturers
    if "Make" in df.columns:
        st.subheader("Top 10 EV Manufacturers")
        top_makes = df["Make"].value_counts().head(10)
        fig2, ax2 = plt.subplots(figsize=(8,4))
        sns.barplot(x=top_makes.values, y=top_makes.index, ax=ax2)
        st.pyplot(fig2)

    # --- Range by Model Year
    if "Model Year" in df.columns and "Electric Range" in df.columns:
        st.subheader("Electric Range by Model Year")
        fig3, ax3 = plt.subplots(figsize=(10,5))
        sns.boxplot(data=df, x="Model Year", y="Electric Range", ax=ax3)
        plt.xticks(rotation=45)
        st.pyplot(fig3)

    # --- State Count
    if "State" in df.columns:
        st.subheader("Top 10 States")
        top_states = df["State"].value_counts().head(10)
        fig4, ax4 = plt.subplots(figsize=(8,4))
        sns.barplot(x=top_states.values, y=top_states.index, ax=ax4)
        st.pyplot(fig4)

# ------------------------------
# PREDICT RANGE
# ------------------------------
elif page == "Predict Range":
    st.title("🔮 Predict Electric Range")

    if model_err:
        st.error("Model not loaded!")
        st.info("Run train_model.py to generate model.pkl & scaler.pkl")
        st.stop()

    year = st.number_input("Model Year", min_value=1995, max_value=2035, value=2022)
    msrp = st.number_input("Base MSRP ($)", min_value=1000, max_value=300000, value=35000)

    if st.button("Estimate Range"):
        try:
            X = [[year, msrp]]
            X_scaled = scaler.transform(X)
            pred = model.predict(X_scaled)[0]
            st.success(f"Estimated Electric Range: **{pred:.1f} miles**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# ------------------------------
# CHATBOT (Gemini)
# ------------------------------
elif page == "Chatbot":
    st.title("🤖 EV Assistant Chatbot")

    api_key = get_api_key()

    if not api_key:
        st.warning("Gemini API key not provided → Using fallback rule-based chatbot.")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_msg = st.text_input("You:", placeholder="Ask something about EVs…")
    c1, c2 = st.columns([1,1])

    if c1.button("Send"):
        if user_msg.strip():
            st.session_state.chat.append(("You", user_msg))
            reply = chat_reply(user_msg, api_key=api_key)
            st.session_state.chat.append(("Assistant", reply))

    if c2.button("Clear Chat"):
        st.session_state.chat = []

    # Display chat
    for sender, msg in st.session_state.chat:
        if sender == "You":
            st.markdown(f"**🧑‍💻 You:** {msg}")
        else:
            st.markdown(f"**🤖 Assistant:** {msg}")

# ------------------------------
# ABOUT
# ------------------------------
elif page == "About":
    st.title("ℹ️ About")

    st.markdown("""
    **EV Smart Analytics & Assistance System**

    Built by **Manikanta (CSE - IoT)**  
    Features:
    - EV Data Analysis
    - ML Range Prediction
    - Gemini-powered AI Chatbot
    """)

    st.code("streamlit run app.py", language="bash")

    st.info("Place datasets inside `/data` folder. Large files should be stored on Google Drive.")

