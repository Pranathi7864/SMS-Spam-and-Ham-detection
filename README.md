# Hybrid SMS Sentinel

## Description

Hybrid SMS Sentinel is an intelligent SMS Spam Detection System developed using Machine Learning and heuristic-based security analysis. The system analyzes incoming SMS messages and classifies them as Spam or Ham (Legitimate). In addition to traditional spam detection, it identifies phishing attempts, suspicious URLs, malicious domains, and unusual messaging behavior to improve detection accuracy and enhance user security.

---

## Features

- SMS Spam and Ham Classification
- TF-IDF Based Text Feature Extraction
- XGBoost Machine Learning Model
- Phishing Link Detection
- Suspicious URL and Domain Identification
- Behavioral Analysis for Repeated Messages
- Confidence Score Prediction
- Real-Time User Interface using Streamlit
- Fast and Accurate Message Analysis

---

## Technologies Used

- Python
- Streamlit
- Scikit-Learn
- XGBoost
- Pandas
- NumPy
- Joblib
- TF-IDF Vectorization

---

## Workflow

1. SMS message is provided by the user.
2. Text preprocessing and feature extraction are performed.
3. TF-IDF converts the message into numerical vectors.
4. Additional security-related features are generated.
5. XGBoost model predicts whether the message is Spam or Ham.
6. Heuristic analysis checks for phishing indicators and suspicious URLs.
7. Behavioral analysis evaluates message frequency and patterns.
8. Final prediction along with confidence score is displayed to the user.

---

## Dataset

The project uses an SMS Spam Collection Dataset containing labeled SMS messages categorized as:

- Spam Messages
- Ham (Legitimate) Messages

The dataset is used to train and evaluate the machine learning model for accurate spam detection and classification.

---

## Outcome

The system provides an efficient and reliable solution for detecting spam and potentially malicious SMS messages. By combining machine learning techniques with security-focused heuristic analysis, the project enhances message filtering accuracy and helps protect users from phishing and spam attacks.
