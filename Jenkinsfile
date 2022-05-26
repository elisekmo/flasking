pipeline {

  environment {
    registry = 'elisekmo/flask_app'
    registryCredentials = 'docker'
    cluster_name = 'skillstorm'
  }
  agent {
    node {
      label 'docker'
    }

  }
  stages {
    stage('git') {
      steps {
        git(url: 'https://github.com/elisekmo/flasking.git', branch: 'main')
      }
    }
    stage('Build Stage') {
      steps {
        script {
          dockerImage = docker.build(registry)
        }
      }
    }
    stage('Deploy Stage') {
      steps {
        script {
          docker.withRegistry('', registryCredentials) {
              dockerImage.push()
          }       
        }
      }
    }
  }
}