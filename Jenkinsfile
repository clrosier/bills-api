pipeline {
    environment {
        registry = "clrosier/bills-api"
        registryCredential = 'dockerhub'
    }

    agent any

    stages {
        stage ('Building image') {
            steps {
                script {
                    image = docker.build registry + ":$VERSION.$BUILD_NUMBER"
                }
            }
        }

        stage ('Push image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        image.push()
                    }
                }
            }
        }
    }
}
