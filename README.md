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
## Challenges Faced
1. Handling Different Types of Input
The system needed to work for both natural language requirements and technical descriptions. Designing logic that works across varied input formats was challenging.

2. Generating Meaningful Test Cases
Initially, the system produced generic test cases. Enhancing it to generate context-aware cases (e.g., login, memory, loops) required careful keyword mapping and logic design.

3. Integrating AI with Rule-Based Logic
Combining a transformer-based NLP model with deterministic rule-based logic required balancing:
AI flexibility
Rule-based accuracy
Ensuring both worked together without conflict was a key challenge.

4. Designing Bug Risk Prediction
Creating a scoring system for risk prediction was difficult, as it required identifying:
High-risk keywords
Assigning appropriate weights
Defining meaningful thresholds

5. Frontend–Backend Communication
Initially faced issues with:
API calls not working
CORS errors
Incorrect data rendering
These were resolved by properly configuring Flask-CORS and debugging API responses.

6. Deployment Challenges
Deploying the project required:
Creating correct configuration files (Procfile, requirements.txt)
Handling environment dependencies
Ensuring compatibility with deployment platforms

7. Debugging and Version Control Issues
While pushing code to GitHub, issues like:
Incorrect repository setup
Merge conflicts
Branch mismatches
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

## Demo Video Link
https://drive.google.com/file/d/1Di028jBa5TE3LtDQwtrJ9BSAXhSNnadT/view?usp=sharing
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
