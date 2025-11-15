# app.py
# ============================================================
# EV SMART ANALYTICS — PREMIUM VERSION (UPGRADED UI)
# ============================================================

import os
import pickle
import time
import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from chatbot import chat_reply  # your chatbot implementation (uses secret API or fallback)
from streamlit_lottie import st_lottie

# ------------------------------------------------------------
# Page config + style
# ------------------------------------------------------------
st.set_page_config(page_title="EV Smart Analytics", page_icon="🔋", layout="wide")
sns.set_style("darkgrid")

UI_CSS = """
<style>
body { background: #0e1117; color: #dfe6e9; }
.user-bubble { background-color: #4e8df5; color: white; padding: 10px 15px; border-radius: 12px; margin: 6px 0px; width: fit-content; max-width: 80%; }
.bot-bubble  { background-color: #232323; color: #ffffff; padding: 10px 15px; border-radius: 12px; margin: 6px 0px; width: fit-content; max-width: 80%; }
.metric-card { background: rgba(255, 255, 255, 0.06); padding: 16px; border-radius: 12px; backdrop-filter: blur(6px); margin: 6px 0px; border: 1px solid rgba(255,255,255,0.06); }
.streamlit-expanderHeader { color: #fff; }
</style>
"""
st.markdown(UI_CSS, unsafe_allow_html=True)

# ------------------------------------------------------------
# Utility helpers
# ------------------------------------------------------------
def load_lottie_url(url: str):
    """Return Lottie JSON from URL or None if failed."""
    if not url:
        return None
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        return None

def typing_effect_generator(text: str, delay: float = 0.01):
    """Generator that yields progressive text for typing effect."""
    out = ""
    for ch in text:
        out += ch
        time.sleep(delay)
        yield out

@st.cache_resource
def load_models():
    """Load ML model & scaler if exist. Returns (model, scaler, err)"""
    try:
        model_path = os.path.join("models", "model.pkl")
        scaler_path = os.path.join("models", "scaler.pkl")
        model = pickle.load(open(model_path, "rb")) if os.path.exists(model_path) else None
        scaler = pickle.load(open(scaler_path, "rb")) if os.path.exists(scaler_path) else None
        if model is None or scaler is None:
            return None, None, "Model or scaler not found in /models"
        return model, scaler, None
    except Exception as e:
        return None, None, str(e)

def safe_load_csv(path: str):
    """Load CSV safely and strip column names."""
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip()
        return df
    except Exception:
        return None

def get_api_key(sidebar_input: str = None):
    """Get API key from sidebar input or Streamlit secrets."""
    if sidebar_input:
        return sidebar_input
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return None

# ------------------------------------------------------------
# Load ML & data
# ------------------------------------------------------------
model, scaler, model_err = load_models()

# ------------------------------------------------------------
# Sidebar (navigation + API key)
# ------------------------------------------------------------
st.sidebar.markdown("<h2>⚡ EV Dashboard</h2>", unsafe_allow_html=True)

# Try to load a stable Lottie for sidebar (safe)
sidebar_lottie = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_jcikwtux.json")
if sidebar_lottie:
    st_lottie(sidebar_lottie, height=160, key="side_lottie")
else:
    st.sidebar.write("🔋 EV Smart Analytics")

page = st.sidebar.radio("", ["Home", "Data Visualization", "Predict Range", "Chatbot", "About"])
st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Gemini API Key (optional)")
api_key_input = st.sidebar.text_input("Enter API Key", type="password", help="Optional: put your GEMINI_API_KEY in .streamlit/secrets.toml for deployment")

# ------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------
if page == "Home":
    st.title("⚡ EV Smart Analytics & Assistance System (Premium UI)")
    # Top Lottie (safe)
    top_lottie = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_cg3wnh0o.json")
    if top_lottie:
        st_lottie(top_lottie, height=240, key="top_lottie")
    st.markdown("### Analyze EV data, visualize insights, predict range, and chat with an AI EV expert!")

    df = safe_load_csv(os.path.join("data", "ev_data.csv"))
    col1, col2, col3 = st.columns(3)
    if df is not None:
        with col1:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Total Records", f"{len(df):,}")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Unique Brands", df["Make"].nunique() if "Make" in df.columns else "N/A")
            st.markdown("</div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Max Range", int(df["Electric Range"].dropna().max()) if "Electric Range" in df.columns else "N/A")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("❗ Dataset not found. Place ev_data.csv in the data/ folder.")

    st.markdown("---")
    st.markdown("**Notes:** If `charging_data.csv` is large (>100MB) keep it on Google Drive and download locally when needed. Use `.streamlit/secrets.toml` for secure keys.")

# ------------------------------------------------------------
# DATA VISUALIZATION
# ------------------------------------------------------------
elif page == "Data Visualization":
    st.title("📊 EV Data Visualization (Enhanced)")
    df = safe_load_csv(os.path.join("data", "ev_data.csv"))
    if df is None:
        st.error("Dataset missing — add `ev_data.csv` to the data/ folder.")
        st.stop()

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    # Range histogram (Plotly)
    if "Electric Range" in df.columns:
        st.subheader("Electric Range Distribution")
        fig = px.histogram(df, x="Electric Range", nbins=40, color_discrete_sequence=["#4e8df5"])
        st.plotly_chart(fig, use_container_width=True)

    # Top manufacturers
    if "Make" in df.columns:
        st.subheader("Top 10 EV Manufacturers")
        top_makes = df["Make"].value_counts().head(10)
        fig2 = px.bar(x=top_makes.values, y=top_makes.index, orientation="h", color_discrete_sequence=["#00c9a7"])
        st.plotly_chart(fig2, use_container_width=True)

    # Range by model year
    if "Model Year" in df.columns and "Electric Range" in df.columns:
        st.subheader("Electric Range by Model Year")
        fig3 = px.box(df, x="Model Year", y="Electric Range", points="outliers", color_discrete_sequence=px.colors.qualitative.Dark24)
        st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------
# PREDICT RANGE
# ------------------------------------------------------------
elif page == "Predict Range":
    st.title("🔮 Predict Electric Range (ML Model)")
    if model_err:
        st.error(f"Model not loaded: {model_err}")
        st.info("Run `train_model.py` locally to create `models/model.pkl` and `models/scaler.pkl`.")
        st.stop()

    c1, c2 = st.columns(2)
    with c1:
        year = st.number_input("Model Year", min_value=1995, max_value=2035, value=2022)
    with c2:
        msrp = st.number_input("Base MSRP ($)", min_value=2000, max_value=200000, value=35000, step=500)

    if st.button("Predict Range"):
        try:
            X = [[year, msrp]]
            X_scaled = scaler.transform(X)
            pred = model.predict(X_scaled)[0]
            st.success(f"Estimated Electric Range: **{pred:.2f} miles**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# ------------------------------------------------------------
# CHATBOT
# ------------------------------------------------------------
elif page == "Chatbot":
    st.title("🤖 EV Assistant Chatbot (Gemini + Typing Animation)")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    api_key = get_api_key(api_key_input)
    if not api_key:
        st.info("No API key found — using fallback rule-based responses.")

    query = st.text_input("You:", placeholder="Ask something like: Best EV for long trips?")
    col_a, col_b = st.columns([1,1])
    with col_a:
        send = st.button("Send")
    with col_b:
        clear = st.button("Clear Chat")

    if clear:
        st.session_state.chat_history = []

    # send
    if send and query and query.strip():
        user_text = query.strip()
        st.session_state.chat_history.append(("You", user_text))
        # call chatbot helper (handles api_key fallback internally)
        try:
            reply = chat_reply(user_text, api_key)
        except Exception as e:
            reply = f"Assistant error: {e}"
        st.session_state.chat_history.append(("Assistant", reply))

    # Render conversation with typing animation for assistant
    for speaker, text in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"<div class='user-bubble'>🧑 {text}</div>", unsafe_allow_html=True)
        else:
            placeholder = st.empty()
            for partial in typing_effect_generator(text, delay=0.008):
                placeholder.markdown(f"<div class='bot-bubble'>🤖 {partial}</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------
elif page == "About":
    st.title("ℹ️ About This Project")
    st.markdown("""
**EV Smart Analytics & Assistance System**  
Built by: **Manikanta – CSE (IoT)**

This app includes EV analytics, ML-based predictions, and an AI-powered chatbot.

**Tech used:** Streamlit, Gemini (optional), Scikit-Learn, Pandas, Plotly, Lottie animations.
""")

# ------------------------------------------------------------
# End of app.py
# ------------------------------------------------------------
