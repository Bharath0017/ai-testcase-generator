from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

classifier = pipeline("text-classification")

def generate_test_cases(input_text):
    test_cases = []
    text = input_text.lower()

    test_cases.append(f"Verify functionality: {input_text}")

    if "login" in text:
        test_cases.append("Test with empty username and password")
        test_cases.append("Test with incorrect credentials")
        test_cases.append("Test with SQL injection input")

    if "array" in text:
        test_cases.append("Test with empty array")
        test_cases.append("Test with large array input")
        test_cases.append("Test with null values")

    if "memory" in text:
        test_cases.append("Test memory leak conditions")
        test_cases.append("Test with large memory allocation")
        test_cases.append("Test memory deallocation")

    if "loop" in text:
        test_cases.append("Test infinite loop condition")
        test_cases.append("Test loop boundary conditions")
        test_cases.append("Test with zero iterations")

    test_cases.append("Test with null input")
    test_cases.append("Test with special characters")

    return test_cases


def predict_bug_risk(input_text):
    score = 0
    text = input_text.lower()

    keywords = {
        "loop": 2,
        "array": 2,
        "pointer": 3,
        "memory": 3,
        "login": 1,
        "authentication": 2
    }

    for key, value in keywords.items():
        if key in text:
            score += value

    if score >= 4:
        return "High Risk"
    elif score >= 2:
        return "Medium Risk"
    return "Low Risk"


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("input", "")

    # 🔥 NEW: keyword detection
    keywords_detected = []
    for key in ["login", "array", "memory", "loop"]:
        if key in text.lower():
            keywords_detected.append(key)

    test_cases = generate_test_cases(text)
    risk = predict_bug_risk(text)

    ai_result = classifier(text)[0]

    return jsonify({
        "test_cases": test_cases,
        "risk": risk,
        "ai_label": ai_result['label'],
        "confidence": float(ai_result['score']),
        "keywords": keywords_detected   # 🔥 NEW OUTPUT
    })


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)