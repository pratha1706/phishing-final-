import random

def predict_image(image_path):
    # Simulate a CNN prediction
    return {
        "label": random.choice(["Phishing", "Legitimate"]),
        "confidence": round(random.uniform(0.6, 0.99), 2)
    }
