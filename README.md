# 🛡️ Phishing Email Detector

A machine learning–powered web app that detects phishing emails and suspicious URLs in real time.

---

## 🚀 Features
- Detects phishing vs. safe emails using a trained ML model  
- Scans and flags suspicious URLs inside the email  
- Logs all detections with timestamps  
- Displays a visual dashboard of phishing activity  

---

## 🧠 Tech Stack
- **Python 3.13**
- **Streamlit** for the web interface  
- **scikit-learn** for ML model  
- **NLTK** for text preprocessing  
- **tldextract** for URL analysis  

---

## 🧩 Project Structure
phishing-detector/
│
├── app.py # Streamlit main app
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── data/
│ ├── phishing_emails.csv
│ └── threat_logs.csv
│
├── model/
│ └── phishing_model.pkl
│
└── src/
├── preprocess.py
├── train_model.py
├── logger.py
└── url_analysis.py


---

## 🧰 Installation & Usage

```bash
# Clone the repo
git clone https://github.com/<your-username>/phishing-detector.git
cd phishing-detector

# Install dependencies
pip install -r requirements.txt

# Train model
python src/train_model.py

# Run Streamlit app
streamlit run app.py

🧩 Example

Paste an email message:

Your account is locked. Verify now: http://paypal-security-login.xyz


App Output:

🚨 This email is potentially malicious!
⚠️ Suspicious URL detected: paypal-security-login.xyz

💡 Future Enhancements

Integrate with PhishTank / VirusTotal APIs

Add email header spoofing detection

Deploy on Streamlit Cloud

---

### 🪜 Step 4 — Initialize Git

Open PowerShell in your project root:

```bash
git init
git add .
git commit -m "Initial commit: Phishing Email Detector"
