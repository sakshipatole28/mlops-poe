pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                checkout scm
            }
        }
        stage('Test with Pytest') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest -v
                '''
            }
        }
        stage('Docker Build and Run') {
            steps {
                sh 'docker build -t hello-mlops:latest .'
                sh 'docker run --rm hello-mlops:latest'
            }
        }
        stage('Evidently Monitor') {
            steps {
                sh '''
                docker run --rm -v "$PWD":/app -w /app python:3.12-slim \
                  sh -c "pip install -r requirements-monitor.txt && python monitor.py && chown $(id -u):$(id -g) evidently_report.html"
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html', allowEmptyArchive: true
        }
    }
}
