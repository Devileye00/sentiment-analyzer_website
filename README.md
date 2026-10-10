# Review Sentiment Analyzer

A Flask web application that classifies a typed review as Positive, Negative, or Neutral using TextBlob sentiment analysis.
Developed for the DevOps ISE-2 assignment using Python, Flask, Git, GitHub, and Jenkins.

## Features
- Web form to enter a review
- Sentiment classification: Positive, Negative, or Neutral
- Sentiment polarity score ranging from -1 to +1
- Automated unit tests using pytest
- Continuous Integration (CI) using Jenkins
- Version control using Git and GitHub
- Optional Ansible deployment files for possible future deployment automation

## Project structure
```
app.py              Flask application and sentiment logic
templates/index.html  Web page
test_app.py         Unit tests
requirements.txt    Python dependencies
Jenkinsfile         Jenkins pipeline configuration
deploy.yml          Optional Ansible deployment playbook
inventory.ini       Optional Ansible inventory
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
| Python | 3.13.1  |
| Flask | 3.0.3 |
| TextBlob | 0.18.0.post0 |
| Gunicorn | 22.0.0 |
| pytest | 8.3.2 |
| Git | 2.55.0.windows.3 |
| Jenkins | 2.568.2 |
| Ansible | Optional; not currently available in the Windows environment |

## CI flow
GitHub Push → Jenkins Checkout → Install Dependencies → Run Tests

Optional Deployment: Ansible deployment files (deploy.yml and inventory.ini) are included for future deployment automation. Ansible deployment is not currently configured in the working Jenkins pipeline.
Jenkins Setup

Open Jenkins and select New Item.

Choose Pipeline and enter a job name.

Select Pipeline script from SCM.

Select Git, enter the GitHub repository URL, and set the branch to */main.

Set Script Path to Jenkinsfile.

Save the job and click Build Now.

Verify that the Checkout, Install Dependencies, and Run Tests stages complete successfully.

Note: GitHub webhook triggering can be configured separately if required. Ansible deployment and its permissions are not part of the current working pipeline.

## Jenkins setup
1. New Item > Pipeline > "Pipeline script from SCM" > Git > paste the GitHub repo URL > branch `main`.
2. Enable "GitHub hook trigger for GITScm polling" (or Poll SCM `H/5 * * * *`).
3. Add a webhook in GitHub: `http://<jenkins-ip>:8080/github-webhook/`.
4. Set Script Path to Jenkinsfile.
5. Save the job and click Build Now.
6. Verify that the Checkout, Install Dependencies, and Run Tests stages complete successfully.

GitHub webhook triggering can be configured separately if required.

## Future Improvements
1. Integrate Ansible for automated deployment.
2. Configure a GitHub webhook to trigger Jenkins builds automatically.