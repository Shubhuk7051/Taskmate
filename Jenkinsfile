pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Shubhuk7051/Taskmate.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}
