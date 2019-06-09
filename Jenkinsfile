
pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'johnmcdevitt/centennial:dev' 
                }
            }
            steps {
                sh 'pip install -r centennial/requirements.txt' 
            }
        }
        
        stage('Test') {
            agent any
            steps {
                sh 'docker build -t centennial centennial/.'
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

        stage('Deploy') {
            when {
                branch 'dockerize'
            }
            agent any
            steps {
                sshagent(credentials :['d17858cb-7026-4eec-bd63-f5e5baeecbc5']) {
                    sh 'ssh -o StrictHostKeyChecking=no john@192.168.1.11 uptime'
                }
            }
        }
    }
}
