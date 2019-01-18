def label = "mypod-${UUID.randomUUID().toString()}"

podTemplate(label: label, containers: [
  containerTemplate(name: 'python-alpine', image: 'ghostgoose33/python-alp:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]
) 
{
def app
def dockerRegistry = "100.71.71.71:5000"
def Creds = "git_cred"
def projName = "get-python"
def imageVersion = "v1"
def imageName = "100.71.71.71:5000/get-service:${imageVersion}"
def imageN = '100.71.71.71:5000/get-service:'


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
        stage("Test code using PyLint and version build"){
			container('python-alpine'){
				pathTocode = pwd()
				sh "python3 ${pathTocode}/sed-python.py template.yml ${dockerRegistry}/get-service ${imageTag}"
				sh "python3 ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"
			}
        }
        stage("Build docker image"){
			container('docker'){
				pathdocker = pwd()
//            app = docker.build("${imageName}:${imageTag}")
				sh "docker build ${pathdocker} -t ${imageN}${imageTag}"
				sh "docker images"
	//withCredentials([usernamePassword(credentialsId: 'docker_registry_2', passwordVariable: 'dockerPassword', usernameVariable: 'dockerUser')]) {
				    
				sh "docker push ${imageN}${imageTag}"
        //}
			}
        }
        stage("Check push image to Docker Registry"){
            pathTocode = pwd()
            sh "python3 ${pathTocode}/images-registry-test.py ${dockerRegistry} ${projName} ${imageTag}"
        }
        stage("Deploy to Kubernetes"){
			container('kubectl'){
				sh "kubectl apply -f template.yml"
				sh "kubectl get pods --namespace=production"
			}
        }
        stage ("E2E Tests - Stage 1"){
            container('python-alpine'){
            sh 'echo "Here are e2e tests"'
	    sh 'python3 e2e-test-prod.py'
          }
        }
	stage ("E2E Tests - Stage 2"){
        //    container('kubectl'){
        //   sh 'kubectl apply -f Kuben.yml'
	//   sh 'kubectl apply -f Kuben(1).yml'
	//   sh 'kubectl get pods -n testing'
        //  }
        }
        stage ("E2E Tests - Stage 3"){
            container('python-alpine'){
            sh 'echo "Here are e2e tests"'
	    sh 'python3 e2e-test-test.py'
          }
        }

    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}


sleep 30
