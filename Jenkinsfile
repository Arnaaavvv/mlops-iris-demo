pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Repository checked out by Jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3.11 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Retrain Model') {
            steps {
                sh 'venv/bin/python retrain.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'iris_model.pkl', fingerprint: true
            }
        }
    }
}
