
# 🛡️ ReviewShield – AI-Based Fake Review Detection System

ReviewShield is an AI-powered web application designed to detect and analyze fake product reviews using Natural Language Processing (NLP) and pattern-based analysis. It not only flags suspicious reviews but also explains the reasoning behind each prediction, helping users make more informed decisions.

---

## 🚀 Features

- 🔍 **Fake Review Detection** using NLP models  
- 🧠 **Sentiment Analysis** to detect overly positive or negative patterns  
- ⚠️ **Explainable AI** – provides reasons for each flagged review  
- 🔁 **Duplicate Review Detection** using similarity algorithms  
- 📊 **Trust Score Calculation** to evaluate overall review authenticity  
- 🌐 **Interactive Web Interface** for real-time analysis  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** Transformers (Hugging Face), TextBlob  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:** Flask-CORS, difflib  

---

## 🧠 How It Works

1. User inputs multiple reviews through the web interface  
2. Backend API processes the reviews using NLP models  
3. Sentiment analysis and rule-based logic detect suspicious patterns  
4. Similarity checks identify duplicate or coordinated reviews  
5. Each review is classified as **Fake** or **Genuine** with explanations  
6. A final **Trust Score** is generated based on overall authenticity  

---

## 📸 Demo

<img width="1812" height="710" alt="image" src="https://github.com/user-attachments/assets/f1e04844-4b6c-4c27-b214-1d4f8eac58a0" />


---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/Ssruvi/reviewshield.git
cd reviewshield

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the backend server
python app.py

### 4. Run frontend
python -m http.server 5500

### 5. Open in browser
http://localhost:5500/index.html
