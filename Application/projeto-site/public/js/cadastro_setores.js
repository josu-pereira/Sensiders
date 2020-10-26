// http://localhost:3333/setor/
// let nome_setor;
// let qtdSensores_setor;
// let contagem;

function retornaSetores(data) {
       var nome_setor = data.map(nomeSetor => nomeSetor.nome);
       var qtdSensores_setor = data.map(qtdSensor => qtdSensor.qtdSensores);
    // todosDados.nome_setor;
    listaSetores(nome_setor,qtdSensores_setor);
    // return todosDados;
}



function listaSetores(nome,setor) {
    for (var i = 0; i < nome.length; i++){
        document.getElementById('listSetores').innerHTML += `
        <tr>
        <td>${nome[i]}</td>
        <td>${setor[i]}</td>
        <td><i data-feather="code" onclick="document.getElementById('divEditarSetor').style.display='block'"></i> </td>
        </tr>
    `;
    }
}

function requisicao() {
    fetch('/setor/1')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // return retornaSetores(data)
            // const todosOsDados = retornaSetores(data);
            return retornaSetores(data);         
        });
}
// for(var i = 0; i < contagem; i++){
//     listaSetores(i);
// }

requisicao();

