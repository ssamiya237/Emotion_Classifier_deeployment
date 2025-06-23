# Emotion_Classifier_deeployment
# Multi-label Emotion Classification API

This repository contains a deployed Flask API that performs multi-label emotion classification on English text inputs using a trained machine learning model.

---

## Features

- Multi-label classification (e.g., sadness, admiration, disgust)
- Trained with TF-IDF + Truncated SVD + custom classifier
- Hosted on Google Cloud Run
- REST API secured with API key

---

## Project Structure

```
.
├── app.py                  # Flask API
├── Dockerfile              # Container definition
├── requirements.txt        # Dependencies
├── model.joblib            # Trained classifier
├── vectorizer.joblib       # TF-IDF transformer
├── svd_model.joblib        # SVD transformer
├── emotion_columns.joblib  # List of emotion labels
└── predict_test.py         # Sample client request script
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/emotion-classifier-api.git
cd emotion-classifier-api
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Locally

```bash
python app.py
```

---

## Testing the API

Send a POST request to `/predict`:

```bash
curl -X POST https://your-api-url.run.app/predict      -H "Content-Type: application/json"      -H "x-api-key: my-super-secret-api-key-2025"      -d '{"input": ["I am sad and disappointed."]}'
```

Or use `predict_test.py` script to send sample inputs.

---

## Docker and GCP Deployment

### Build Docker Image

```bash
gcloud builds submit --tag gcr.io/ml-deployment-project-463620/ml-api
```

### Deploy to Cloud Run

```bash
gcloud run deploy ml-api   --image gcr.io/ml-deployment-project-463620/ml-api   --platform managed   --region us-central1   --allow-unauthenticated   --set-env-vars API_KEY=my-super-secret-api-key-2025
```

---

## Known Challenges

- Model failed to detect some emotions with default threshold.
- Resolved by lowering threshold to `0.1` for higher recall in emotion detection.

---

## Author

Samiya Sarwar  
Seneca Polytechnic | AIG 200  
