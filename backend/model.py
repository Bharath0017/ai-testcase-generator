from transformers import pipeline

# Load NLP model
classifier = pipeline("text-classification")

def analyze_text(text):
    result = classifier(text)[0]
    return result['label'], result['score']