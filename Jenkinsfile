
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
                sh 'docker-compose build'
                sh 'docker-compose up -d'
                sh 'docker exec web cd /app/centennial && python manage.py test -v 2'
            }
        }
    }
}
