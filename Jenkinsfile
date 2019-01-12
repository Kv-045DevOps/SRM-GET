node
{
    def app
    def docketRegistry = ""
    def Creds = "maxcred"
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
            sh "python ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
