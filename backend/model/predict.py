import pickle
import pandas as pd
from pathlib import Path

# import the ml model
PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_FILE = PROJECT_ROOT / "backend" / "model" / "model.pkl"

with open(MODEL_FILE, 'rb') as f:
    model = pickle.load(f)

# versioning
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # Create mapping: {class_name: probability}
    class_probs = {
        label: round(prob, 4)
        for label, prob in zip(class_labels, probabilities)
    }

    return {
        'predicted_category': predicted_class,
        'confidence': confidence,
        'class_probabilities': class_probs
    }
