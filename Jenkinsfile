pipeline {

    environment {
        registry = "clrosier/bills-api"
        registryCredential = 'dockerhub'
    }

    agent {
        docker {
            image 'docker:dind'
        }
    }
    stages {
        stage ('Build') {
            steps {
                echo 'Build the docker image'

                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
    }
}
