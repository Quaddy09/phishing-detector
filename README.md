# 🛡️ Phishing URL Detector (Machine Learning Project)

## 🔍 Overview
This project is a **Phishing URL Detection System** built using **Python**, **Machine Learning**, and **NLP techniques**.  
It automatically classifies URLs as **Legitimate** or **Phishing**, helping identify potential cyber threats early.  
The goal is to showcase cybersecurity, data preprocessing, and model training skills.

---

## ⚙️ Features
- ✅ Detects phishing URLs using a trained ML model  
- 🧠 Uses Natural Language Processing for URL feature extraction  
- 📊 Achieves high accuracy with Logistic Regression  
- 💾 Saves model as `.pkl` for future inference  
- 🔄 Easy to retrain with new datasets  

---

## 🧰 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Machine Learning | Scikit-learn |
| NLP | NLTK |
| Data Handling | Pandas, NumPy |
| Model Storage | Joblib |
| Environment | VS Code, PowerShell |
| Version Control | Git + GitHub |

---

## 📂 Project Structure
phishing-detector/
│
├── data/
│ └── phishing_site_urls.csv # Dataset
│
├── model/
│ └── phishing_model.pkl # Trained model
│
├── src/
│ ├── train_model.py # Training script
│ └── predict.py # Prediction script
│
├── requirements.txt # Python dependencies
└── README.md # Documentation

---

## 🚀 How to Run Locally

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Quaddy09/phishing-detector.git
cd phishing-detector
