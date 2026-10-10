
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Tools') {
            steps {
                bat '"C:\\Users\\Vishwajeet Shinde\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
                bat 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Vishwajeet Shinde\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Sentiment Analyzer: build and tests passed!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
