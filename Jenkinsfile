
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
            agent {
                docker {
                    image 'johnmcdevitt/centennial:dev'
                }
            steps {
                sh 'cd centennial'
                sh 'python manage.py test -v 2'
            }
        }
    }
}
