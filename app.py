import streamlit as st
import time
import random

# Set up page
st.set_page_config(page_title="Quotex Bot Interface", layout="centered")

# Custom CSS for the "Neon/Dark" look
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    .signal-card {
        background-color: #1a1f2e;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #3d3d5c;
        margin-top: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #3b82f6;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    .neon-text { color: #00ffcc; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# UI Elements
st.image("https://cdn-icons-png.flaticon.com/512/2830/2830253.png", width=100)
st.title("REAL SIGNAL BOT")
st.markdown("---")

# Inputs
col1, col2 = st.columns(2)
asset = col1.selectbox("ASSET", ["USD/INR(OTC)", "EUR/USD", "BTC/USD", "ETH/USD"])
timer = col2.selectbox("TIMER", ["10 SEC", "30 SEC", "1 MIN", "5 MIN"])

# Signal Generation Logic (Simulation)
if 'signal' not in st.session_state:
    st.session_state.signal = None

if st.button("GET SIGNAL"):
    with st.spinner('Analyzing market...'):
        time.sleep(1.5) # Simulate processing
        st.session_state.signal = {
            "type": random.choice(["BUY", "SELL"]),
            "confidence": random.randint(75, 98),
            "time": 10
        }

# Display Results Card
if st.session_state.signal:
    sig = st.session_state.signal
    color = "green" if sig["type"] == "BUY" else "red"
    
    st.markdown(f"""
    <div class="signal-card">
        <h2 style="color:{color};">{sig["type"]}</h2>
        <p>CONFIDENCE</p>
        <h1 style="color:white;">{sig["confidence"]}%</h1>
        <p>Timer: {sig["time"]}s</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("USE 1 STEP MTG (Martingale) - RISK MANAGEMENT ADVISED")

# Footer
st.markdown("<br><br><center>To join group click here</center>", unsafe_allow_html=True)
