def label = "mypod-${UUID.randomUUID().toString()}"
def dockerRegistry = "100.71.71.71:5000"
def Creds = "git_cred"

String e2e_YAML = """ """
String get = "${params.imageTagGET_}"
String ui = "${params.imageTagUI_}"
String db = "${params.imageTagDB_}"

properties([
    parameters([
	stringParam(
            defaultValue: '***', 
            description: '', 
            name: 'service')
    ])
])

podTemplate(label: label, annotations: [podAnnotation(key: "sidecar.istio.io/inject", value: "false")], containers: [
  containerTemplate(name: 'python-alpine', image: 'ghostgoose33/python-alp:v3', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'ghostgoose33/docker-in:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'helm', image: 'ghostgoose33/kubectl_helm:v1', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
], serviceAccount: "jenkins") 
{


node(label)
{
    try{
        stage("Pre-Test"){
            dir('get'){
            git(branch: "test", url: 'https://github.com/Kv-045DevOps/SRM-GET.git', credentialsId: "${Creds}")
            imageTagUI = (sh (script: "git rev-parse --short HEAD", returnStdout: true))
            tmp = "1"
            pathTocodeget = pwd()
            }
        }
        stage("E2E Test - Stage 1"){
            container('helm'){
                sh "helm upgrade --install --namespace testing --force e2e-testing-db ${pathTocodeget}/List-Helm-Charts/e2e-testing-db --set=deploy.version=v1,image.tag.db=${db}"
                sh "helm upgrade --install --namespace testing --force e2e-testing-get ${pathTocodeget}/List-Helm-Charts/e2e-testing-get --set=deploy.version=v1,image.tag.get=${get}"
                sh "helm upgrade --install --namespace testing --force e2e-testing-ui ${pathTocodeget}/List-Helm-Charts/e2e-testing-ui --set=deploy.version=v1,image.tag.ui=${ui}"
                sh "kubectl get pods --namespace=testing"
            }
        }
        sleep 40
        stage ("E2E Tests - Stage 2"){
            container('python-alpine'){
            	sh 'echo "Here is e2e test"'
	        sh "python3 /e2e-test-test.py"
          }
        }

	stage ("Deploy"){
            
		build(job: 'test_deploy', parameters: [[$class: 'StringParameterValue', name:"imageTagGET_", value: "${params.imageTagGET_}"],
		[$class: 'StringParameterValue', name:"imageTagUI_", value: "${params.imageTagUI_}"],
		[$class: 'StringParameterValue', name:"imageTagDB_", value: "${params.imageTagDB_}"],
		[$class: 'StringParameterValue', name:"imageTagPOST_", value: "${params.imageTagPOST_}"],
		[$class: 'StringParameterValue', name:"service", value: "${params.service}"]], wait: true)
        }
        
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}
