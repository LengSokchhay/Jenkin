pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/LengSokchhay/Jenkin.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'python', url: 'https://github.com/LengSokchhay/Jenkin.git'
                sh 'python3 my_module.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
