import streamlit as st
import joblib
import numpy as np
from utils.heuristics import get_technical_features
import hashlib
from datetime import datetime, timedelta
import time
st.set_page_config(page_title="Hybrid SMS Sentinel", page_icon="🛡️")


if "message_log" not in st.session_state:
    st.session_state.message_log = []

TRUSTED_DOMAINS = [
     "amazon", "google", "paypal", "microsoft",
    "apple", "facebook", "instagram",
    "bank", "icici", "hdfc", "sbi"
]


@st.cache_resource
def load_models():
    try:
        model = joblib.load('models/xgboost_model.pkl')
        tfidf = joblib.load('models/tfidf_vectorizer.pkl')
        return model, tfidf
    except FileNotFoundError:
        return None, None

model, tfidf = load_models()

if model is None:
    st.error("⚠️ Train model first using train_model.py")
    st.stop()


# ---------------- HASH FUNCTION ----------------
def get_message_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


# ---------------- TEMPORAL DETECTION ----------------
def check_frequency(message):
    now = datetime.now()
    message_hash = get_message_hash(message)

    # Remove old entries (older than 5 minutes)
    st.session_state.message_log = [
        entry for entry in st.session_state.message_log
        if now - entry["time"] < timedelta(minutes=5)
    ]

    # Count including current
    count = sum(
        1 for entry in st.session_state.message_log
        if entry["hash"] == message_hash
    ) + 1

    st.session_state.message_log.append({
        "hash": message_hash,
        "time": now
    })

    return count


st.title("🛡️ Hybrid SMS Sentinel")
st.markdown("---")

message = st.text_area(
    "Enter the SMS message to scan:",
    height=150,
    placeholder="Paste suspicious message here..."
)

if st.button("Scan Message"):

    if message.strip():

        tech = get_technical_features(message)

        text_vec = tfidf.transform([message]).toarray()

        math_features = np.array([[ 
            tech['entropy'],
            tech['digit_count'],
            tech['has_url'],
            tech['length'],
            tech['risky_tld'],
            tech['phish_score'],
            tech['symbol_ratio'],
            tech['impersonation_score']
        ]])

        X_final = np.hstack((text_vec, math_features))


        start = time.time()
        prediction = model.predict(X_final)
        end = time.time()

        print("Inference time:", end - start, "seconds")
        prediction = model.predict(X_final)
        probability = model.predict_proba(X_final)[0][1]

        frequency_count = check_frequency(message)
        behavior_flag = frequency_count >= 3

        ai_flag = (prediction[0] == 1)
        sensor_flag = (tech['risky_tld'] == 1 or tech['phish_score'] >= 1)
        


        st.subheader("Analysis Result")

        if behavior_flag:
            st.error("🚨 SPAM DETECTED (High Frequency Pattern)")

        elif ai_flag or sensor_flag:
            st.error(f"🚨 SPAM DETECTED (Confidence: {probability:.2%})")

        else:
            st.success(f"✅ MESSAGE IS SAFE (Confidence: {1-probability:.2%})")

        with st.expander("See Technical Details"):
            st.write("Entropy:", tech['entropy'])
            st.write("Digit Count:", tech['digit_count'])
            st.write("Risky TLD:", tech['risky_tld'])
            st.write("Symbol Ratio:", tech['symbol_ratio'])
            st.write("Frequency (5 min window):", frequency_count)

            if tech['final_url']:
                st.write("Final URL:", tech['final_url'])

    else:
        st.warning("Please enter text to analyze.")
    
