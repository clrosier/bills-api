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
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
    }
}
