pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git branch: 'main', url:'https://github.com/Shubhuk7051/Taskmate.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        echo "Build the Image of Web App."
        sh 'sudo docker build -t taskmate .'
      }
    }
    stage('Push to Docker Hub') {
      steps {
        echo "Push the Image of Web App to Docker Hub."
        withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass", usernameVariable:"dockerHubUser")]){
        sh "sudo docker tag taskmate-app ${env.dockerHubUser}/taskmate-app:v1"
        sh "sudo docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
        sh "sudo docker push ${env.dockerHubUser}/taskmate-app:v1"
      }
    }
  }
  stage('Deploy') {
    steps {
      echo "Deploy the Container."
      sh 'sudo docker-compose down && docker-compose up -d'
    }
  }
}
