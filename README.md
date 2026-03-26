# 🚀 AI Test Case Generator & Bug Predictor

## 📌 Overview
This project is an AI-powered automation testing tool that generates test cases and predicts bug-prone areas from software requirements or code snippets. It combines rule-based logic with Natural Language Processing (NLP) to improve testing efficiency and coverage.

---

## 🧩 Problem Statement
Manual software testing is time-consuming, repetitive, and often fails to cover edge cases. Developers also struggle to identify high-risk areas in code, leading to bugs in production.

---

## 💡 Solution Approach
The system takes a requirement or code input and:
- Analyzes it using an NLP model
- Detects important keywords (e.g., login, memory, loop, array)
- Generates context-aware test cases
- Predicts bug risk using a scoring mechanism

---

## 🚀 Key Features
- ✅ Automatic test case generation  
- ✅ Context-aware edge case detection  
- ✅ Bug risk prediction (Low / Medium / High)  
- ✅ AI-based text classification (Transformers)  
- ✅ Keyword extraction for explainability  
- ✅ Simple and interactive UI  

---

## 🧠 How It Works
1. User enters a requirement or code snippet  
2. System processes input using:
   - Rule-based logic (for test cases)
   - NLP model (for classification)  
3. Outputs:
   - Test cases  
   - Risk level  
   - AI label & confidence  
   - Detected keywords  

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Model:** HuggingFace Transformers  
- **Libraries:** Flask-CORS, Torch  
- **Deployment:** Gunicorn, Render  

---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-testcase-generator.git
cd backend
python3 app.py
open index.html