pipeline {
  agent any
  stage ('Select'){
    choice1 = input( id: 'userInput', message: 'Select your choice', parameters: [ [\$class: 'ChoiceParameterDefinition', choices: 'aa\nbb', description: '', name: ''] ])
    if(choice1.equals("aa")){
        choice2 = input( id: 'userInput', message: 'Select your choice', parameters: [ [\$class: 'ChoiceParameterDefinition', choices: 'yy\nww', description: '', name: ''] ])
    }else{
        choice2 = input( id: 'userInput', message: 'Select your choice', parameters: [ [\$class: 'ChoiceParameterDefinition', choices: 'gg\nkk', description: '', name: ''] ])
    }
}
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
