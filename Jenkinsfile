pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/2025sl93022/labsheet1-2025sl93022.git'
            }
        }
 
        stage('Build') {
            steps {
                sh 'echo "Build Stage"'
            }
        }
 
        stage('Test') {
            steps {
                sh '''
                python3 calculator.py
                '''
            }
        }
 
        stage('Deploy') {
            steps {
                sh 'echo "Deploy Stage"'
            }
        }
    }
}
