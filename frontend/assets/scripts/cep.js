const cepInp = document.querySelector('#cep');
const ruaInp = document.querySelector('#rua');
const cidadeInp = document.querySelector('#cidade');
const ufInp = document.querySelector('#uf');

const buscaCep = (evt) => {
        const cepUsuario = evt.target.value;

        if (cepUsuario.length != 8) {
            return;
        }

        fetch(`https://viacep.com.br/ws/${cepUsuario}/json/`)
        .then( (resposta) => {return resposta.json()})
        .then( (dados) => {
            ruaInp.value = dados.logradouro;
            cidadeInp.value = dados.localidade;
            ufInp.value = dados.uf;
            cepInp.value = dados.cep;
        })
}
cepInp.oninput = buscaCep;

// fetch('https://viacep.com.br/ws/02235001/json/')
// .then((resposta) => { return resposta.json() })
// .then((dados) => { console.log(dados);
// })