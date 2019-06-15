
pipeline {
    agent none
    stages {
        stage('Build') { 
            agent any
            steps {
                sh 'docker build -t johnmcdevitt/centennial-dev:$BRANCH_NAME.$BUILD_NUMBER centennial/.'
            }
        }
        
        stage('Test') {
            agent any
            steps {

                sh 'docker ps'
                sh 'docker stack deploy --compose-file centennial/docker-compose.yml test'
                sh 'docker ps'
                retry(2) {
                    script {
                        try {
                            sh 'docker exec test_web.1.$(docker service ps -f "name=test_web.1" test_web -q --no-trunc | head -n1) python manage.py test -v 2'
                        }
                        catch (e) {
                            echo 'Failed to run unit tests'
                            sleep {
                                time 5
                                unit seconds
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy to PROD') {
            when {
                branch 'dockerize'
            }
            agent any
            steps {
                sshagent(credentials :['jenkins-deploy-john-ubuntu']) {
                    sh '''
                    ssh john@192.168.1.11 ls
                    '''
                }
            }
        }
    }
}
