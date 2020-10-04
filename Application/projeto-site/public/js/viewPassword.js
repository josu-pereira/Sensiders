let eye = document.querySelector('#eye')
let pwd = document.querySelector('#txtSenha')

function onSenha(){
    pwd.type = "text"
    eye.src = "../../img/icons/eye-off.svg"
    eye.onclick = function(){
        offSenha()
    }
}

function offSenha(){
    pwd.type = "password"
    eye.src = "../../img/icons/eye.svg"
    eye.onclick = function(){
        onSenha()
    }
}