
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
            agent none
            steps {
                sh '''
                    docker-compose build
                    docker-compose up -d
                    docker exec web cd /app/centennial && python manage.py test -v 2
                    '''
            }
        }
    }
}
