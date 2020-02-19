pipeline {

    environment {
        registry = "clrosier/bills-api"
        registryCredential = 'dockerhub'
    }

    node {
        def image = docker.build registry
        sh 'docker image ls'
    }
}
