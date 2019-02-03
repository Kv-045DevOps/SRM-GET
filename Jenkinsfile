def label = "mypod-${UUID.randomUUID().toString()}"


podTemplate(label: label, containers: [
  containerTemplate(name: 'python-alpine', image: 'ghostgoose33/python-alp:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'ghostgoose33/docker-in:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
], serviceAccount: "jenkins") 
{

def dockerRegistry = "100.71.71.71:5000"
def Creds = "git_cred"
def projName = "get-service"
def imageVersion = "v2"
def imageName = "100.71.71.71:5000/get-service:${imageVersion}"
def imageN = '100.71.71.71:5000/get-service:'

node(label)
{
    try{
        stage("Pre-Test"){
            dir('get'){
            git(branch: "test", url: 'https://github.com/Kv-045DevOps/SRM-GET.git', credentialsId: "${Creds}")
            imageTagGET = (sh (script: "git rev-parse --short HEAD", returnStdout: true))
            tmp = "1"
            //imageTagGET = sh(returnStdout: true, script: "git tag -l --points-at HEAD").trim()
            pathTocodeget = pwd()
            }
        }
        stage("Test image_regisrty_check"){
            container("python-alpine"){
                check_new = (sh (script: "python3 ${pathTocodeget}/images-registry-test.py get-service ${imageTagGET}", returnStdout:true).trim())
                echo "${check_new}"
            }
        }
        if ("${tmp}" == "${check_new}"){
            echo "YES"
        } else {
            echo "NO"
        }
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint and version build"){
			container('python-alpine'){
				pathTocode = pwd()
				//sh "python3 ${pathTocode}/sed_python.py template.yaml ${dockerRegistry}/get-service ${params.imageTag}"
				//sh "python3 ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"
			}
        }
        stage("Build docker image"){
			container('docker'){
				pathdocker = pwd()
				//sh "docker build ${pathdocker} -t ${imageN}${params.imageTag}"
				//sh "docker images"
                //sh "cat /etc/docker/daemon.json"
				//sh "docker push ${imageN}${params.imageTag}"
			}
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}
