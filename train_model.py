import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from utils.heuristics import get_technical_features
from sklearn.metrics import accuracy_score, precision_score
# Load dataset
df = pd.read_csv("dataset/spam.csv", encoding="latin-1")
df = df[['v1', 'v2']]
df.columns = ['label', 'text']

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Extract heuristic features
feature_list = []

for text in df['text']:
    tech = get_technical_features(text)

    feature_list.append([
        tech['entropy'],
        tech['digit_count'],
        tech['has_url'],
        tech['length'],
        tech['risky_tld'],
        tech['phish_score'],
        tech['symbol_ratio'],
        tech['impersonation_score']
    ])

X_math = np.array(feature_list)

# TF-IDF
tfidf = TfidfVectorizer(max_features=3000)
X_text = tfidf.fit_transform(df['text']).toarray()

# Combine features
X = np.hstack((X_text, X_math))
y = df['label'].values

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/xgboost_model.pkl")
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

print("Model trained and saved successfully!")
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
