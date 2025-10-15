# src/model.py (part 1)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv("data/cleaned_emails.csv")

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['clean_text'])
y = df['label']

# Save vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ TF-IDF vectorizer saved as vectorizer.pkl")

# src/model.py (part 2)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("✅ Model Evaluation:")
print(classification_report(y_test, y_pred))

# Save trained model
joblib.dump(model, "model.pkl")
print("✅ Model saved as model.pkl")
