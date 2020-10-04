// let eye = document.querySelector('#eye')
// let pwd = document.querySelector('#txtSenha')

function onSenha(input, icon){
    let pwd = document.getElementById(input)
    let eye = document.getElementById(icon)
    pwd.type = "text"
    eye.src = "../../img/icons/eye.svg"
    eye.onclick = function(){
        offSenha(input, icon)
    }
}

function offSenha(input, icon){
    let pwd = document.getElementById(input)
    let eye = document.getElementById(icon)
    pwd.type = "password"
    eye.src = "../../img/icons/eye-off.svg"
    eye.onclick = function(){
        onSenha(input, icon)
    }
}