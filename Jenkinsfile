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

        stage('Deploy Model') {
            steps {
                sh 'install -m 644 iris_model.pkl /home/arnnavvvv/app/iris_model.pkl'
                sh 'sudo /usr/bin/systemctl restart ml-api'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'iris_model.pkl', fingerprint: true
            }
        }
    }
}
