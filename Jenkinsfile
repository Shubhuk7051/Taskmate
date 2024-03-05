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
        sh 'docker build -t taskmate-app .'
      }
    }
    stage('Push to Docker Hub') {
      steps {
        echo "Push the Image of Web App to Docker Hub."
        withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass", usernameVariable:"dockerHubUser")]){
        // sh "docker tag taskmate-app ${env.dockerHubUser}/taskmate-app:v1"
        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
        // sh "docker push ${env.dockerHubUser}/taskmate-app:v1"
      }
    }
  }
    // stage('Deploy') {
    //   steps {
    //     echo "Deploy the Container."
    //     sh 'docker-compose down && docker-compose up -d'
    //   }
    // }
  }
}
