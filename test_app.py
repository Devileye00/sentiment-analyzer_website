from app import app, analyze_sentiment


def test_positive():
    assert analyze_sentiment("This product is amazing and wonderful")[0] == "Positive"


def test_negative():
    assert analyze_sentiment("This is terrible, awful and a waste of money")[0] == "Negative"


def test_neutral():
    assert analyze_sentiment("The package arrived on Tuesday")[0] == "Neutral"


def test_predict_endpoint():
    client = app.test_client()
    res = client.post("/predict", json={"review": "I love this, it is great"})
    assert res.status_code == 200
    assert res.get_json()["sentiment"] == "Positive"


def test_empty_review():
    client = app.test_client()
    res = client.post("/predict", json={"review": "  "})
    assert res.status_code == 400
