from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text):
    """Return (label, polarity) for the given review text."""
    polarity = TextBlob(text).sentiment.polarity  # -1.0 to +1.0
    if polarity > 0.1:
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
        return jsonify({"error": "Please enter a review first."}), 400
    label, polarity = analyze_sentiment(review)
    return jsonify({"sentiment": label, "polarity": polarity})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
