
//email
const emailRegex = /[^@]+@[^\.]+\..+/g

//numero da casa
const numberRegex = /^[0-9]{0,4}/gm

//cep
const cepRegex = /^\d{5}-\d{3}$/g

//cidade e rua
const lettersRegex = /[a-zA-Z\u00C0-\u00FF ]+/i

// uf
const ufRegex = /[a-zA-Z]{2}/i

//senha forte
// 1 – (?=.*[0-9]) Verifica se existe um número;
// 2 – (?=.*[a-z]) Verifica se existe uma letra minúscula;
// 3 – (?=.*[A-Z]) Verifica se existe uma letra maiúscula;
// 4 – ([a-zA-Z0-9]{8,}) Verifica se existe pelo menos 8 caracteres entre os digitados.
const pwRegex = /^([a-zA-Z0-9!@*#]{8,15})$/g;

// evitar q a pagina recarregue com loading
var form = document.querySelector('form');
form.addEventListener('submit', function(e){
    e.preventDefault(); 
})

function loginValidationForm() {

    var email = document.getElementById('txtEmail').value;
    var senha = document.getElementById('txtSenha').value;

    if (email == "" || email == null || senha == "") {
        return alert("Por Favor, Preencha o email!");
    } else {
        if (emailRegex.test(email) === false) {
            return alert("Por Favor, Insira um email valido!");
        }
    }
    // if (pwRegex.test(senha) === false) {
    //     return alert("Por Favor, Insira a senha correta!");
    //     return false;
    // }
}

function forgotPasswordForm() {
    var email = document.getElementById('emailPwInp').value;

    if (email == "" || email == null) {
        return alert("Por Favor, Insira um email valido!");
    } else {
        if (emailRegex.test(email) === false) {
            return alert("Por Favor, Insira um email valido!");
        }
    }

    recuperarSenha();
}

function registerForm() {
    var cepInp = document.getElementById('cep').value;
    var numeroInp = document.getElementById('numero').value;
    var ruaInp = document.getElementById('rua').value;
    var cidadeInp = document.getElementById('cidade').value;
    var ufInp = document.getElementById('uf').value;
    var emailInp = document.getElementById('email').value;
    var senhaInp = document.getElementById('senha').value;
    var confirmInp = document.getElementById('confirm_senha').value;

    if (cepInp == "" || cepInp == null) {
        return alert("Por Favor, Preencha o CEP !");
    } else {
        if (cepRegex.test(cepInp) === false) {
            return alert("Por Favor, Insira um CEP valido!");
        }
    }
    if (numeroInp == "" || numeroInp == null) {
        return alert("Por Favor, Insira um Numero valido!");
    } else {
        if (numberRegex.test(numeroInp) === false) {
            return alert("Por Favor, Insira um Numero valido!");
        }
    }
    if (ruaInp == "" || ruaInp == null) {
        return alert("Por Favor, Insira um Rua valido!");
    } else {
        if (lettersRegex.test(ruaInp) === false) {
            return alert("Por Favor, Insira um rua valido!");
        }
    }
    if (cidadeInp == "" || cidadeInp == null) {
        return alert("Por Favor, Insira um cidade valido!");
    } else {
        if (lettersRegex.test(cidadeInp) === false) {
            return alert("Por Favor, Insira um cidade valido!");
        }
    }
    if (ufInp == "" || ufInp == null) {
        return alert("Por Favor, Insira um UF valido!");
    } else {
        if (ufRegex.test(ufInp) === false) {
            return alert("Por Favor, Insira um UF valido!");
        }
    }
    if (emailInp == "" || emailInp == null) {
        return alert("Por Favor, Insira um email valido!");
    } else {
        if (emailRegex.test(emailInp) === false) {
            return alert("Por Favor, Insira um email valido!");
        }
    }
    if (senhaInp == "" || senhaInp == null) {
        return alert("Por Favor, Insira uma senha  valido!");
    } else {
        if (pwRegex.test(senhaInp) === false) {
            return alert("A senha deve conter no minimo 8 caracteres ate 15");
        }
    }
    if (confirmInp == "" || confirmInp == null) {
        return alert("Por Favor, Insira um confirmInp valido!");
    } else {
        if (pwRegex.test(confirmInp) === false) {
            return alert("A senha deve conter no minimo 8 caracteres ate 15");
        }
    }
    if (senhaInp != confirmInp) {
        return alert("as senhas devem ser iguais");
    }

    cadastrar();
}