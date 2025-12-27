pipeline {
    agent any
    
    stages {
        stage('Test Script') {
            steps {
                sh 'chmod +x count_files.sh'
                sh 'bash -n count_files.sh'
                sh './count_files.sh || true'
            }
        }

        stage('Build RPM') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                dnf install -y rpm-build rpmdevtools
                rpmdev-setuptree

                cp count_files.sh ~/rpmbuild/SOURCES/
                
                cp ${WORKSPACE}/rpm/count_files.spec ~/rpmbuild/SPECS/
                rpmbuild -bb ~/rpmbuild/SPECS/count_files.spec

                cp ~/rpmbuild/RPMS/noarch/*.rpm ${WORKSPACE}/
                '''
            }
        }

        stage('Build DEB') {
            agent {
                docker {
                    image 'ubuntu:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                apt-get update
                apt-get install -y build-essential debhelper devscripts

                mkdir -p build/count-files-1.0
                cp count_files.sh build/count-files-1.0/
                cp -r debian build/count-files-1.0/

                cd build/count-files-1.0
                chmod +x debian/rules
                dpkg-buildpackage -us -uc -b

                cp ../*.deb ${WORKSPACE}/
                '''
            }
        }

        stage('Test RPM Installation') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                dnf install -y which
                rpm -ivh count-files-*.rpm
                which count_files
                rpm -e count-files
                '''
            }
        }

        stage('Test DEB Installation') {
            agent {
                docker {
                    image 'ubuntu:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                dpkg -i count-files_*.deb || apt-get install -f -y
                
                which count_files.sh
                
                apt-get remove -y count-files
                '''
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully'
        }
        failure {
            echo 'Build failed'
        }
        always {
            cleanWs()
        }
    }
}
