    // evitar q a pagina recarregue com loading
    var form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        e.preventDefault();
    })

    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    btn.onclick = function () {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    
    // function calcular() {
    //     var dois = 2;
    //     var sensorValor = 50;        
    //     var sensor = parseInt(document.getElementById('sensorInp')) *sensorValor;
    //     var setor = parseInt(document.getElementById('setorInp'));
    //     var entradaSaida = parseInt(document.getElementById('entradaInp'));
    //     var caixas = parseInt(document.getElementById('caixasInp')) * 50;

    //     iValorSensor.innerHTML = `R$ ${sensor.toFixed(2)}`;
    //     iSetor.innerHTML = `${setor}`;
    //     iMercado.innerHTML = `${entradaSaida}, dois sensores  por cada dá:${(sensor*sensorValor)*entradaSaida}`;
    //     iCaixas.innerHTML = `${caixas}, um sensor por caixa: ${caixas*sensorValor}`;
    // }