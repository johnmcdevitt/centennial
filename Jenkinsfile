
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
                sh 'docker exec test_web.1 cd /app/centennial && python manage.py test -v 2'
            }
        }
    }
}
