from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


# Phrases used to identify explicit sentiment
NEGATIVE_PHRASES = [
    "don't like",
    "do not like",
    "very disappointed",
    "too short",
    "waste of money",
    "disappointed with the quality",
    "feels cheap",
    "doesn't look durable",
    "does not look durable",
    "unhappy with this purchase",
    "not worth the money",
    "not good",
    "not satisfied",
    "disappointed with the quality",
    "poor quality",
    "low quality",
    "bad quality",
    "feels cheap",
    "cheap material",
    "poorly made",
    "bad experience",
    "not worth the money",
    "waste of money",
    "too expensive",
    "stopped working",
    "doesn't work",
    "does not work",
    "broken",
    "damaged",
    "defective",
    "uncomfortable",
    "unhappy with this purchase",
    "doesn't last",
    "does not last",
    "doesn't look durable",
    "does not look durable",
    "not as expected",
    "below expectations",
    "terrible",
    "awful",
    "worst",
    "dislike",
    "quality is poor",
    "poor",
    "bad quality",
    "low quality",
    "price has increased",
    "price increased",
    "price went up",
    "more expensive",
    "paying more",
    "not happy about the price",
    "too expensive",
    "price is too high",
    "costs more than yesterday",
    "price hike",
]

POSITIVE_PHRASES = [
    "love it",
    "really good",
    "very good",
    "excellent",
    "highly recommend",
    "very satisfied",
    "great quality",
    "good quality",
    "well made",
    "well-made",
    "good value",
    "worth the money",
    "great experience",
    "works perfectly",
    "easy to use",
    "comfortable",
    "looks amazing",
    "looks great",
    "beautiful design",
    "very happy",
    "exceeded my expectations",
    "better than expected",
    "impressed with",
    "smells amazing",
    "long lasting",
    "long-lasting",
    "durable",
    "fantastic",
    "wonderful",
    "perfect",
]

NEUTRAL_PHRASES = [
    "arrived yesterday",
    "arrived today",
    "comes in",
    "available in",
    "has three",
    "has two",
    "measures",
    "weighs",
    "the package contains",
    "the box includes",
    "available in different colors",
    "the product includes",
]
   
def analyze_sentiment(text):
    """Return the sentiment label and TextBlob polarity."""
    text_lower = text.lower()
    polarity = TextBlob(text).sentiment.polarity

    has_negative = any(
        phrase in text_lower for phrase in NEGATIVE_PHRASES
    )
    has_positive = any(
        phrase in text_lower for phrase in POSITIVE_PHRASES
    )

    if has_negative and has_positive:
        label = "Mixed"
    elif has_negative:
        label = "Negative"
    elif has_positive:
        label = "Positive"
    elif polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    return label, round(polarity, 3)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    review = (data.get("review") or "").strip()

    if not review:
        return jsonify({
            "error": "Please enter a review first."
        }), 400

    label, polarity = analyze_sentiment(review)

    return jsonify({
        "sentiment": label,
        "polarity": polarity
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)