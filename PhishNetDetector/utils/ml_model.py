import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    # Load dataset
    phishing_urls = pd.read_csv("data/phishing_urls.csv")
    legitimate_urls = pd.read_csv("data/legitimate_urls.csv")

    # Combine datasets
    phishing_urls['label'] = 1
    legitimate_urls['label'] = 0
    data = pd.concat([phishing_urls, legitimate_urls])

    # Feature extraction
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['url'])
    y = data['label']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save model
    with open("models/phishing_model.pkl", "wb") as f:
        pickle.dump((model, vectorizer), f)

def predict_url(url):
    # Load model
    with open("models/phishing_model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)

    # Predict
    X = vectorizer.transform([url])
    prediction = model.predict(X)
    return "Phishing URL" if prediction[0] == 1 else "Legitimate URL"