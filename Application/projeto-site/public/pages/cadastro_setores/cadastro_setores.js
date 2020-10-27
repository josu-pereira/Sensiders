// http://localhost:3333/setor/
// let nome_setor;
// let qtdSensores_setor;
// let contagem;
function fnVerificarNumero() {
    var texto2 = Number(document.getElementById('inputEdit2').value);

    if (texto2.length == 1 && isNaN(texto2)) {
        alert("ta no if");
    } else {
        for (i = 0; i < texto2.length; i++) {
            if (isNaN(texto2[i])) {
                texto2 = texto2.substring(0, i);
            }
        }
    }
}

function fnSalvar() {
    var nomeSetor = document.getElementById('inputEdit1').value;
    var qtdSensores = Number(document.getElementById('inputEdit2').value);
    var idSetor = localStorage.getItem('idSetor');

    if (isNaN(qtdSensores)) {
        alert("Insira um valor numérico válido");
    }
    // if(texto1 == "" || texto1 == null) {
    //     return alert("Por Favor, Preencha o novo nome do Setor !");
    // }
    // if(texto2 == "" || texto2 == null) {
    //     return alert("Por Favor, Preencha a quantidade de Sensores !");
    // }

    fetch(`http://localhost:3333/setor/editar/${idSetor}`, {
        header: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({
            nomeSetor,
            qtdSensores
        })
    }).then((response) => {
        console.log(response);
    });

}

function requisicao() {
    var idFilial = localStorage.getItem("idFilial");
    fetch(`/setor/${idFilial}`)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // return retornaSetores(data)
            // const todosOsDados = retornaSetores(data);
            console.log(data)
            data.forEach(item => {
                document.getElementById('listSetores').innerHTML += `
                    <tr>
                        <td>${item.nome}</td>
                        <td>${item.qtdSensores}</td>
                        <td><svg onclick="openModal(${item.idSetor})" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit" onclick="document.getElementById('divEditarSetor').style.display='block'"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg> </td>
                    </tr>
                `;

            });


        });
}

function openModal(idSetor) {
    document.getElementById('divEditarSetor').style.display = 'block';
    console.log(idSetor);
    localStorage.setItem('idSetor', idSetor);
    fetch(`/setor/all/${idSetor}`)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // return retornaSetores(data)
            // const todosOsDados = retornaSetores(data);
            console.log(data)
            data.forEach(item => {
                document.getElementById('inputEdit1').value = item.nome;
                document.getElementById('inputEdit2').value = item.qtdSensores;
            });


        });
}

window.onload = requisicao();