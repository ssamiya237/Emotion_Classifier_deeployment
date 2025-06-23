# Emotion_Classifier_deployment
# Emotion Classifier API Deployment

This project demonstrates the end-to-end process of developing, containerizing, and deploying a multi-label emotion classification model using machine learning and Google Cloud Platform (GCP). The application is served via a Flask API on **Cloud Run**, with secure API key authentication.

---

## Problem Overview

The objective is to classify one or more emotions from a given input sentence. This is a **multi-label text classification** problem where each sentence can express multiple emotions (e.g., sadness, disgust, admiration, etc.).

---

## ML Pipeline

- **Data Preprocessing:**
  - Vectorization using TF-IDF
  - Dimensionality reduction using Truncated SVD

- **Model Training:**
  - Multi-label model using `OneVsRestClassifier` with `XGBoost` as base estimator
  - Emotions included:  
    `['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']`

- **Model Artifacts:**
  - `model.joblib` – Final trained classifier
  - `vectorizer.joblib` – TF-IDF vectorizer
  - `svd_model.joblib` – SVD model
  - `emotion_columns.joblib` – Emotion label columns

---

## Containerization (Docker)

The API is containerized using Docker.  
You can build and test it locally using:

```bash
docker build -t emotion-api .
docker run -p 5000:5000 emotion-api
```

---

## GCP Deployment (Cloud Run)

Deployment commands used:

```bash
# Step 1: Submit Docker image
gcloud builds submit --tag gcr.io/ml-deployment-project-463620/ml-api

# Step 2: Deploy to Cloud Run
gcloud run deploy ml-api \
  --image gcr.io/ml-deployment-project-463620/ml-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars API_KEY=my-super-secret-api-key-2025
```

**Live Endpoint:**  
`https://ml-api-1055958174760.us-central1.run.app/predict`

**Auth Required:**  
Header must include `x-api-key: my-super-secret-api-key-2025`

---

## Sample API Request (Python)

```python
import requests

url = "https://ml-api-1055958174760.us-central1.run.app/predict"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "my-super-secret-api-key-2025"
}
payload = {
    "input": [
        "I am sad and disappointed.",
        "You are amazing!",
        "That was really exciting!",
        "I feel so embarrassed and nervous.",
        "This is disgusting!"
    ]
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

---

## Challenges Faced

- Initially, emotion predictions were too strict due to a high threshold for multi-label classification.
- After analysis, a **threshold of 0.1** was chosen to increase the sensitivity of predictions and allow detection of more subtle or multiple emotions per input.
- Cloud Run logs and testing were used to tune this decision iteratively.

---

## Repository Structure

```
.
├── ML_deployment.ipynb        # Model training & evaluation notebook
├── app.py                     # Flask app to serve predictions
├── Dockerfile                 # Container definition
├── requirements.txt           # Python dependencies
├── model.joblib               # Trained model
├── vectorizer.joblib          # TF-IDF vectorizer
├── svd_model.joblib           # SVD dimensionality reducer
├── emotion_columns.joblib     # List of output emotion labels
└── README.md                  # This file
```

---

## Project Completed Features

- Model training and evaluation
- Containerization via Docker
- Deployment to GCP Cloud Run with secure API key
- API endpoint tested and functioning
- Repository includes all artifacts and documentation

---

## 👩‍💻 Author

**Samiya Sarwar**  
GitHub: [@ssamiya237](https://github.com/ssamiya237)
