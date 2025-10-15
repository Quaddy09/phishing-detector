import streamlit as st
import joblib
import pandas as pd
from src.preprocess import clean_email
from src.logger import log_threat, LOG_FILE
from src.url_analysis import analyze_urls  # 👈 new import

st.set_page_config(page_title="Phishing Detector", layout="wide")
st.title("🔒 Phishing Email Detector with URL Analysis")

st.write("Paste an email message below to check for phishing or malicious URLs.")

user_input = st.text_area("Email content")

if st.button("Analyze"):
    model = joblib.load("model/phishing_model.pkl")
    cleaned = clean_email(user_input)
    prediction = model.predict([cleaned])[0]

    # ✅ Analyze URLs
    suspicious_urls = analyze_urls(user_input)

    # ✅ Log the threat
    log_threat(user_input, prediction)

    if prediction == 1 or len(suspicious_urls) > 0:
        st.error("🚨 This email is potentially **malicious**!")
    else:
        st.success("✅ This email seems safe.")

    # Show details about URLs
    if suspicious_urls:
        st.warning("⚠️ Suspicious URLs detected:")
        for s in suspicious_urls:
            st.write(f"🔗 {s['url']} — *{s['reason']}*")
    else:
        st.info("No suspicious URLs found.")

st.divider()
st.subheader("📊 Threat Activity Dashboard")

try:
    df = pd.read_csv(LOG_FILE)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Analyzed", len(df))
    with col2:
        st.metric("Phishing Detected", len(df[df['prediction'] == 'phishing']))

    st.bar_chart(df['prediction'].value_counts())
    with st.expander("View detailed logs"):
        st.dataframe(df)
except Exception:
    st.info("No logs yet — analyze an email to get started.")
