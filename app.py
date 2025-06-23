from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)


API_KEY = "my-super-secret-api-key-2025"


model = joblib.load("model.joblib")  
vectorizer = joblib.load("vectorizer.joblib")  
svd = joblib.load("svd_model.joblib") 
emotion_labels = joblib.load("emotion_columns.joblib") 


@app.route("/", methods=["GET"])
def home():
    return "ML Emotion Classifier API is running."


@app.route("/predict", methods=["POST"])
def predict():
   
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data or "input" not in data:
        return jsonify({"error": "Missing 'input' key"}), 400

    texts = data["input"]

 
    X_tfidf = vectorizer.transform(texts)
    X_svd = svd.transform(X_tfidf)

   
    threshold = 0.1
    probas = model.predict_proba(X_svd)
    predictions = (probas > threshold).astype(int)

    
    output = []
    for row in predictions:
        labels = [emotion_labels[i] for i, val in enumerate(row) if val == 1]
        output.append(labels)

    return jsonify({"prediction": output})
