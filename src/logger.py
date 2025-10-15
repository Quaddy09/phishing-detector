import csv
from datetime import datetime
import os

LOG_FILE = "data/threat_logs.csv"

# Ensure the folder exists
os.makedirs("data", exist_ok=True)

# Create file with headers if it doesn’t exist yet
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "email_snippet", "prediction"])

def log_threat(email_text, prediction):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            email_text[:80].replace("\n", " "),  # short preview
            "phishing" if prediction == 1 else "safe"
        ])