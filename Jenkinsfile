def label = "mypod-${UUID.randomUUID().toString()}"

//imagePullSecrets:['myregistrysecret']

podTemplate(label: label, containers: [
  containerTemplate(name: 'jenkins-slave', image: 'ghotsgoose33/jenkins-slave:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
]) 
{
def app
//def dockerRegistry = "192.168.213.128:5000"
def Creds = "git_cred"
def projName = "get-python"
def imageVersion = "v1"
def imageName = "ghostgoose33/get-python:${imageVersion}"
def imageN = 'ghostgoose33/get-python:'


node(label)
{
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
//        stage("Test code using PyLint"){
//            pathTocode = pwd()
//            sh "python3.6 ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"
//        }
        stage("Build docker image"){
			container('docker'){
				pathdocker = pwd()
//            app = docker.build("${imageName}:${imageTag}")
				sh "docker build ${pathdocker} -t ${imageName}"
				sh "docker images"
				withCredentials([usernamePassword(credentialsId: 'docker_registry', passwordVariable: 'dockerPassword', usernameVariable: 'dockerUser')]) {
				sh "docker login -u ${env.dockerUser} -p ${env.dockerPassword}"
				sh "docker push ${imageName}"
        }
			}
        }
        stage("Push to remote(test) Docker Registry"){
        //
        }
        stage("Check push image to Docker Registry"){
        //    sh "pip install requests"
            pathTocode = pwd()
        //    sh "python3.4 ${pathTocode}/images-registry-test.py ${dockerRegistry} ${projName} ${imageTag}"
        }
        stage("Deploy to Kubernetes"){
			container('kubectl'){
				sh("sed -i.bak 's#${imageN}${imageVersion}#ghostgoose33/get-python:${imageVersion}#' jenkins-pod.yaml")
			//	sh "kubectl apply -f jenkins-pod.yaml"
			//	sh "sudo kubectl get pods --namespace=stark-cluster"
				sh "kubectl get pods --namespace=stark-cluster"
			}
        }
	stage ("Unit Tests"){
            sh 'echo "Here will be e2e tests"'
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}
