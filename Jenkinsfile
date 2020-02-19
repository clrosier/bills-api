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
        stage ('Checkout') {
            steps {
                echo 'Checkout out code from GitHub...'

            }
        }
    }
}
