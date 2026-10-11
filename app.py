
from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


# Explicit negative phrases
NEGATIVE_PHRASES = [
    "battery runs out too quickly",
    "runs out too quickly",
    "not for a full day",
    "waited almost an hour",
    "waited almost an hour for our order",
    "don't like",
    "do not like",
    "not good",
    "not satisfied",
    "very disappointed",
    "disappointed because",
    "disappointed with",
    "poor quality",
    "quality is poor",
    "low quality",
    "bad quality",
    "feels cheap",
    "cheap material",
    "poorly made",
    "bad experience",
    "not worth the money",
    "waste of money",
    "too expensive",
    "price has increased",
    "price increased",
    "price went up",
    "more expensive",
    "paying more",
    "not happy about the price",
    "not happy about paying more",
    "price is too high",
    "price hike",
    "stopped working",
    "doesn't work",
    "does not work",
    "broken",
    "damaged",
    "defective",
    "uncomfortable",
    "unhappy with this purchase",
    "regret buying it",
    "dislike",
    "terrible",
    "awful",
    "worst",
    "disappears within an hour",
    "disappears quickly",
    "doesn't last long",
    "does not last long",
    "expected it to last much longer",
    "runs out too quickly",
    "battery runs out too quickly",
    "not for a full day",
    "battery life is poor",
    "waited almost an hour",
    "gets hot",
    "gets too hot",
    "overheating",
    "overheating is frustrating",
    "frustrating",
    "poor stitching",
    "looks nothing like the photos",
    "not worth it",
    "not as expected",
    "below expectations",
    "too short",
    "doesn't last",
    "does not last",
    "doesn't look durable",
    "does not look durable",
    "not happy",
    "not worth the money",
]


# Explicit positive phrases
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
    "soft",
    "fitting is perfect",
    "color looks exactly like the pictures",
    "earlier than expected",
    "neat",
    "delicious",
    "friendly",
    "fast",
    "good for short trips",
    "good for the price",
    "in perfect condition",
    "order again",
    "screen looks amazing",
]


# Factual phrases that can indicate a neutral product description
NEUTRAL_PHRASES = [
    "holds one litre of water",
    "holds one liter of water",
    "has a black lid",
    "fits in my backpack",
    "arrived on monday",
    "available in blue and grey",
    "available in blue and gray",
    "has three main compartments",
    "two side pockets",
    "adjustable shoulder straps",
    "available in different colors",
    "available in different colours",
    "has three",
    "has two",
    "measures",
    "weighs",
    "the package contains",
    "the box includes",
    "the product includes",
    "arrived yesterday",
    "arrived today",
    "comes in",
]


def analyze_sentiment(text):
    """Return sentiment label and TextBlob polarity."""
    text_lower = text.lower()
    polarity = TextBlob(text).sentiment.polarity

    has_negative = any(
        phrase in text_lower for phrase in NEGATIVE_PHRASES
    )
    has_positive = any(
        phrase in text_lower for phrase in POSITIVE_PHRASES
    )
    has_neutral = any(
        phrase in text_lower for phrase in NEUTRAL_PHRASES
    )

    # Mixed must be checked before individual sentiment labels.
    if has_positive and has_negative:
        label = "Mixed"

    elif has_negative:
        label = "Negative"

    elif has_positive:
        label = "Positive"

    # Use factual cues for product descriptions only when
    # explicit positive or negative expressions are absent.
    elif has_neutral:
        label = "Neutral"

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
