import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from preprocess import load_and_prepare_data

print("Loading and cleaning data...")
X_train, X_test, y_train, y_test = load_and_prepare_data()

model = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=3000, stop_words='english')),
    ('clf', MultinomialNB())
])

print("Training model...")
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

# ✅ Automatically create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/phishing_model.pkl")
print("✅ Model saved to model/phishing_model.pkl")
