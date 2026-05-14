from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from textblob import TextBlob
from difflib import SequenceMatcher

app = Flask(__name__)
CORS(app)

# Load ML model
classifier = pipeline("text-classification")

def analyze_review(review):
    reasons = []

    # ML prediction
    result = classifier(review)[0]
    label = result['label']
    score = result['score']

    # ✅ FIX 1: YOU FORGOT SENTIMENT
    sentiment = TextBlob(review).sentiment.polarity

    # Rules (explainability)
    if sentiment > 0.8:
        reasons.append("Extreme positive sentiment")

    if review.count("!") > 2:
        reasons.append("Excessive punctuation")

    if len(review.split()) < 3:
        reasons.append("Too short review")

    if review.lower().count("best") > 1:
        reasons.append("Repetitive wording")

    # Final decision logic
    is_fake = False
    if "POSITIVE" in label and (sentiment > 0.8 or len(reasons) > 1):
        is_fake = True

    # ✅ FIX 2: INDENTATION
    return {
        "review": review,
        "prediction": "Fake" if is_fake else "Genuine",
        "confidence": round(score * 100, 2),
        "reasons": reasons,
        "sentiment": round(sentiment, 2)
    }


# ✅ FIX 3: REMOVE DUPLICATE ROUTE
@app.route("/analyze", methods=["GET", "POST"])
def analyze():

    # similarity function
    def is_similar(a, b):
        return SequenceMatcher(None, a, b).ratio() > 0.8

    if request.method == "GET":
        return "API is working!"

    data = request.json
    reviews = data.get("reviews", [])

    results = [analyze_review(r) for r in reviews]

    # detect similar reviews
    for i in range(len(results)):
        for j in range(i+1, len(results)):
            if is_similar(results[i]["review"], results[j]["review"]):
                results[i]["reasons"].append("Similar to another review")
                results[j]["reasons"].append("Duplicate pattern")

    # trust score
    genuine_count = sum(1 for r in results if r["prediction"] == "Genuine")
    trust_score = (genuine_count / len(results)) * 100 if results else 0

    return jsonify({
        "trust_score": round(trust_score, 2),
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)