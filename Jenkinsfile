node
{
    def app
    def dockerRegistry = "192.168.213.128:5000"
    def Creds = ""
    def projName = "get-python"
    def imageVersion = "v1"
    def imageName = "192.168.213.128:5000/get-python:${imageVersion}.${env.BUILD_NUMBER}"
    def imageN = '192.168.213.128:5000/get-python:'
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
            sh "echo ${env.BUILD_NUMBER}"
        }
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint"){
            sh "pip3 install pylint"
            pathTocode = pwd()
            sh "python3.6 ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"
        }
        stage("Build docker image"){
            pathdocker = pwd()
//            app = docker.build("${imageName}:${imageTag}")
            sh "docker build ${pathdocker} -t ${imageName}"
            sh "docker images"
        }
        stage("Push to remote(test) Docker Registry"){
        withCredentials([usernamePassword(credentialsId: 'docker_registry', passwordVariable: 'dockerPassword', usernameVariable: 'dockerUser')]) {
            sh "docker login -u ${env.dockerUser} -p ${env.dockerPassword} ${dockerRegistry}"
            sh "docker push ${imageName}"
        }
        }
        stage("Check push image to Docker Registry"){
            sh "pip install requests"
            pathTocode = pwd()
            sh "python3.6 ${pathTocode}/images-registry-test.py ${dockerRegistry} ${projName} ${imageTag}"
        }
        stage("Deploy to Kubernetes"){
            sh("sed -i.bak 's#${imageN}${imageVersion}#${imageName}#' jenkins-pod.yaml")
            sh "kubectl apply -f jenkins-pod.yaml --kubeconfig=kubeconfig"
            sh "sudo kubectl get pods --namespace=jenkins-srv --kubeconfig=KUBECONFIG"
        }
	stage ("Unit Tests"){
            sh 'echo "Here will be e2e tests"'
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
