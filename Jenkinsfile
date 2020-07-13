pipeline {
    agent any

    environment {
        registryCredential = 'hub-docker'
        devImage = ''
    }

    stages {

        stage('Build DEV container') {
            steps {
                script {
                    devImage = docker.build('johnmcdevitt/centennial-dev:$BRANCH_NAME.$BUILD_NUMBER', 'centennial/')
                }
            }
        }


        stage('Deploy Test') {
            steps {
                sh 'docker ps'
                // set version and deploy test environment
                sh 'DEV_VERSION=$BRANCH_NAME.$BUILD_NUMBER NGINX_PORTS="8080:8080" docker stack deploy --compose-file centennial/docker-compose.yml test'

                // give time for deployment hard code 1 minute
                sleep(time:60,unit:"SECONDS")

                retry(3) {
                    script {
                        try {
                            sh 'docker ps'
                            sh 'docker exec test_web.1.$(docker service ps -f "name=test_web.1" test_web -q --no-trunc | head -n1) python manage.py test -v 2'
                        }
                        catch (e) {
                            echo 'Failed to run unit tests'
                            sleep {
                                time 10
                                unit seconds
                            }
                        }
                    }
                }
            }
        }

        // insert parallel static tests here

        stage('Push DEV container') {
            steps {
                script {
                    docker.withRegistry('', registryCredential ) {
                        devImage.push()
                    }
                }
            }
        }

        stage('Deploy to PROD') {
            when {
                branch 'master'
            }
            steps {
                sshagent(credentials :['jenkins-deploy-john-ubuntu']) {
                    sh '''
                    scp centennial/docker-compose.yml john@192.168.1.11:/tmp
                    ssh john@192.168.1.11 DEV_VERSION=$BRANCH_NAME.$BUILD_NUMBER NGINX_PORTS="80:80" docker stack deploy -c /tmp/docker-compose.yml test
                    '''

                     retry(3) {
                        script {
                            try {
                                sleep(time:30,unit:"SECONDS")
                                sh '''
                                ssh john@192.168.1.11 docker ps
                                ssh john@192.168.1.11 docker exec test_web.1.$(ssh john@192.168.1.11 docker service ps -f "name=test_web.1" test_web -q --no-trunc | head -n1) python manage.py migrate
                                '''
                            }
                            catch (e) {
                                echo "Failed attempting database migrations"
                            }
                        }
                    }
                }
            }
        }
    }
}
