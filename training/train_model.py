import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("data.csv")

X = data["text"]
y = data["priority"]

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "../saved_model/priority_model.pkl")

print("Model trained and saved successfully")
