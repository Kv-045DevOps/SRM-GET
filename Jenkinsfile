node('centos')      //using label for remote agent(optional, will be change)
{
    def app
    def dockerRegistry = "192.168.213.128:5000"    //This is address of my Docker Regisrty. After install "prod" Docker Registry this URL will be change
    def Creds = "###"  //credential for GitHub account
    def projName = "get-python"
    def imageName = '192.168.213.128:5000/get-python'
    try{
        stage("Git Checkout"){
            git(
                branch: "MZhovanik",
                url: 'https://github.com/Kv-045DevOps/SRM-GET.git',
                credentialsId: "${Creds}")
            sh "git rev-parse --short HEAD > .git/commit-id"
            imageTag= readFile ".git/commit-id"
        }
        stage("Info"){
            sh "echo ${imageTag}"
        }
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint"){
            sh "pip install pylint"
            pathTocode = pwd()
            sh "python3.4 ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"     //Python version will be change on version in Jenkins master instance
        }
        stage("Build docker image"){
            pathdocker = pwd()
//            app = docker.build("${imageName}:${imageTag}")
            sh "docker build ${pathdocker} -t ${imageName}:${imageTag}"
            sh "docker images"
        }
        stage("Push to remote(testing) Docker Registry"){
        withCredentials([usernamePassword(credentialsId: 'docker_registry', passwordVariable: 'dockerPassword', usernameVariable: 'dockerUser')]) {
            sh "docker login -u ${env.dockerUser} -p ${env.dockerPassword} ${dockerRegistry}"
            sh "docker push ${imageName}:${imageTag}"
        }
        }
        stage("Check push image to Docker Registry"){
            sh "pip install requests"
            pathTocode = pwd()
            sh "python3.4 ${pathTocode}/images-registry-test.py ${dockerRegistry} ${projName} ${imageTag}"  //Python version will be change on version in Jenkins master instance 
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
