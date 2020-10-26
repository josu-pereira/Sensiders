// http://localhost:3333/setor/
// let nome_setor;
// let qtdSensores_setor;
// let contagem;

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
                        <td><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit" onclick="document.getElementById('divEditarSetor').style.display='block'"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg> </td>
                    </tr>
                `;
                
            });

            
        });
}

window.onload = requisicao();