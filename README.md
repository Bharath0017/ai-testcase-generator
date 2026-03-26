# AI Test Case Generator & Bug Predictor

## Overview
This project is an AI-powered automation testing tool that generates test cases and predicts bug-prone areas from software requirements or code snippets. It combines rule-based logic with Natural Language Processing (NLP) to improve testing efficiency and coverage.

---

## Problem Statement
Manual software testing is time-consuming, repetitive, and often fails to cover edge cases. Developers also struggle to identify high-risk areas in code, leading to bugs in production.

---

## Solution Approach
The system takes a requirement or code input and:
- Analyzes it using an NLP model  
- Detects important keywords (e.g., login, memory, loop, array)  
- Generates context-aware test cases  
- Predicts bug risk using a scoring mechanism  

---

## Key Features
- Automatic test case generation  
- Context-aware edge case detection  
- Bug risk prediction (Low / Medium / High)  
- AI-based text classification (Transformers)  
- Keyword extraction for explainability  
- Simple and interactive UI  

---

## How It Works
1. User enters a requirement or code snippet  
2. Backend processes input using:
   - Rule-based logic (test case generation)  
   - NLP model (classification)  
3. Outputs:
   - Test cases  
   - Risk level  
   - AI label & confidence  
   - Detected keywords  

---

## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Model:** HuggingFace Transformers  
- **Libraries:** Flask-CORS, Torch  
- **Deployment:** Gunicorn, Render  

---

## Project Structure

project/
│── backend/
│ └── app.py
│
│── frontend/
│ └── index.html
│
│── README.md
│── requirements.txt
│── Procfile

---
##  How to Run Locally
---

### 1. Clone the repository
## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-testcase-generator.git
cd backend

 2.Install dependencies
pip install -r requirements.txt

3.Run backend
cd backend
python3 app.py

4.Run frontend
Open frontend/index.html in your browser

5.Sample Input
Handle memory allocation in loop

6.Sample Output
Risk: High Risk  
AI Label: NEGATIVE  
Confidence: 0.88  
Keywords: memory, loop  

Test Cases:
- Verify functionality: Handle memory allocation in loop
- Test memory leak conditions
- Test with large memory allocation
- Test memory deallocation
- Test infinite loop condition
- Test loop boundary conditions
- Test with zero iterations
- Test with null input
- Test with special characters
---
