import joblib

model = joblib.load("saved_model/priority_model.pkl")

def predict_priority(text: str) -> str:
    return model.predict([text])[0]
