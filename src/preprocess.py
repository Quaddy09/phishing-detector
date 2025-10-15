# src/preprocess.py

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split

# download NLTK resources (run once)
nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_email(text):
    if isinstance(text, float):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+', 'url', text)           # replace URLs
    text = re.sub(r'\S+@\S+', 'emailaddr', text)     # replace email addresses
    text = re.sub(r'\d+', 'number', text)            # replace numbers
    text = re.sub(r'\W', ' ', text)                  # remove punctuation
    words = [ps.stem(w) for w in text.split() if w not in stop_words]
    return ' '.join(words)

# Load your dataset
def load_and_prepare_data(path="data/phishing_emails.csv"):
    df = pd.read_csv(path)
    df['text'] = df['text'].apply(clean_email)
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Assume the dataset has columns: "text", "label" (1 = phishing, 0 = legit)
def clean_and_save_data(path="data/phishing_emails.csv", out_path="data/cleaned_emails.csv"):
    df = pd.read_csv(path)
    df['clean_text'] = df['text'].apply(clean_email)
    df.to_csv(out_path, index=False)
    print(f"✅ Data cleaned and saved to {out_path}")

# Uncomment the following line to run the cleaning and saving process
# clean_and_save_data()
