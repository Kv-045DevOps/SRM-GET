def label = "mypod-${UUID.randomUUID().toString()}"


podTemplate(label: label, annotations: [podAnnotation(key: "sidecar.istio.io/inject", value: "false")], containers: [
  containerTemplate(name: 'python-alpine', image: 'ghostgoose33/python-alp:v3', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'ghostgoose33/docker-in:v1', command: 'cat', ttyEnabled: true)
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

properties([
    parameters([
	stringParam(
            defaultValue: '*', 
            description: 'TAG_Change', 
            name: 'service')
    ])
])


node(label)
{
    try{
        stage("Pre-Test"){
            dir('get'){
            git(branch: "test", url: 'https://github.com/Kv-045DevOps/SRM-GET.git', credentialsId: "${Creds}")
            imageTagGET = (sh (script: "git rev-parse --short HEAD", returnStdout: true))
            tmp = "1"
            pathTocodeget = pwd()
            }
        }
        stage("Test image_regisrty_check"){
            container("python-alpine"){
                check_new = (sh (script: "python3 /images-registry-test.py get-service ${imageTagGET}", returnStdout:true).trim())
                echo "${check_new}"
		echo "${imageTagGET}"
		echo "${params.imageTagGET_}"
            }
        }
        
        stage ("Unit Tests"){
            sh 'echo "Here will be unit testss"'
        }
        stage("Test code using PyLint and version build"){
			container('python-alpine'){
				//sh "python3 ${pathTocodeget}/sed_python.py template.yaml ${dockerRegistry}/get-service ${imageTag}"
				sh "python3 /pylint-test.py ${pathTocodeget}/app/app.py"
			}
        }
        stage("Build docker image"){
			container('docker'){
				pathdocker = pwd()
                                if ("${tmp}" == "${check_new}"){
                                	sh "docker build ${pathTocodeget} -t ${imageN}${imageTagGET}"
					sh "docker images"
                                	sh "cat /etc/docker/daemon.json"
					sh "docker push ${imageN}${imageTagGET}"
					sleep 20
					build(job: 'GitHub/GET-SERVICES/test1', parameters: [[$class: 'StringParameterValue', name:"imageTagGET_", value: "${imageTagGET}"],
									   [$class: 'StringParameterValue', name:"imageTagUI_", value: "${params.imageTagUI_}"],
									   [$class: 'StringParameterValue', name:"imageTagDB_", value: "${params.imageTagDB_}"],
									   [$class: 'StringParameterValue', name:"imageTagPOST_", value: "${params.imageTagPOST_}"],
									   [$class: 'StringParameterValue', name:"service", value: "get"]], wait: true)
        			} else {
            				echo "NO"
        			}
				
			}
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}
