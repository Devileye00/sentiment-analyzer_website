# Review Sentiment Analyzer

A Flask web app that classifies a typed review as **Positive**, **Negative** or **Neutral** using TextBlob (NLP / machine learning based sentiment analysis).
Built for the DevOps ISE-2 assignment with Git, GitHub, Jenkins and Ansible.

## Features
- Web form to enter a review
- Sentiment label plus polarity score (-1 to +1)
- Unit tests with pytest
- CI/CD with Jenkins, deployment with Ansible

## Project structure
```
app.py              Flask application and sentiment logic
templates/index.html  Web page
test_app.py         Unit tests
requirements.txt    Python dependencies
Jenkinsfile         Jenkins pipeline
deploy.yml          Ansible playbook
inventory.ini       Ansible inventory
```

## Run locally
```
python -m venv venv
venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Run tests
```
pytest -v
```

## Versions used
| Tool | Version |
|------|---------|
| Python | 3.x (fill in: `python --version`) |
| Flask | 3.0.3 |
| TextBlob | 0.18.0.post0 |
| Gunicorn | 22.0.0 |
| pytest | 8.3.2 |
| Git | fill in: `git --version` |
| Jenkins | fill in (Manage Jenkins > About Jenkins) |
| Ansible | fill in: `ansible --version` |

## CI/CD flow
GitHub push -> Jenkins (Checkout -> Install -> Test) -> Ansible playbook deploys the app on port 5000.

## Jenkins setup
1. New Item > Pipeline > "Pipeline script from SCM" > Git > paste the GitHub repo URL > branch `main`.
2. Enable "GitHub hook trigger for GITScm polling" (or Poll SCM `H/5 * * * *`).
3. Add a webhook in GitHub: `http://<jenkins-ip>:8080/github-webhook/`.
4. The `jenkins` user needs passwordless sudo for Ansible (`sudo visudo`: `jenkins ALL=(ALL) NOPASSWD: ALL`).
