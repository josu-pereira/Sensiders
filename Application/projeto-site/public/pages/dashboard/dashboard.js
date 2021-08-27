
// Para abrir e fechar o filtro do heatmap-tempo
openFilterOption = true;
function openFilter() {

    if(openFilterOption) {
        document.querySelector('.heatmap-form-content').style.display = "block";
        document.querySelector('.filter').classList.add("current");
        openFilterOption = false;
    } else {
        document.querySelector('.heatmap-form-content').style.display = "none";

        // document.querySelector('.filter').className += " aaa"
        document.querySelector('.filter').classList.remove("current");
        openFilterOption = true;
    }

    console.log(openFilterOption)
}


function verifyLoadingPage() {
    
    if(localStorage.getItem("loadingPage")) {
    
        document.querySelector('.loading-page').style.display = "none";
        document.querySelector('.header-top').style.display = "block";
        document.querySelector('.container-main').style.display = "flex";
    
    }

}

window.onload = verifyLoadingPage();

tempoLoadingPage = setTimeout(() => {

    document.querySelector('.loading-page').style.display = "none";
    document.querySelector('.header-top').style.display = "block";
    document.querySelector('.container-main').style.display = "flex";

    localStorage.setItem("loadingPage", true);

    clearTimeout(tempoLoadingPage);

}, 2000);








let setorCB = 1;


function mudarSetor() {
    setorCB = setor_cb.value;
    obterDadosGraficoLinha();
}
//Config. do heatmap
var heatmapInstance = h337.create({
    container: document.querySelector(".heatmap"),
});
var heatmapInstanceTempo = h337.create({
    container: document.querySelector(".heatmap-tempo"),
});

function buscarPresencas(json) {
    console.log(json);
    var points = [];
    var max = 100;
    var min = 0;
    var width = 850;
    var height = 490;
    let maiorMov = {
        MediaMinuto: 0,
        nome: ''
    };
    let menorMov = {
        MediaMinuto: 100,
        nome: ''
    };
    let mediaMov = 0;

    heatmapInstance.setData({
        data: []
    });

    for (let i = 0; i < json.length; i++) {
        maiorMov = json[i].MediaMinuto > maiorMov.MediaMinuto ? json[i] : maiorMov;
        menorMov = json[i].MediaMinuto < menorMov.MediaMinuto ? json[i] : menorMov;
        mediaMov += json[i].MediaMinuto;
    }
    mediaMov = mediaMov / json.length;

    maiorMov_p.innerHTML = maiorMov.nome;
    menorMov_p.innerHTML = menorMov.nome;
    mediaMov_p.innerHTML = mediaMov.toFixed(1);

    //Gerando um ponto por local da planta
    const locais = [{
            x: 60,
            y: 60,
            value: json[0].MediaMinuto,
            radius: 70,
        },
        {
            x: 200,
            y: 60,
            value: json[1].MediaMinuto,
            radius: 60,
        },
        {
            x: 340,
            y: 60,
            value: json[2].MediaMinuto,
            radius: 70,
        },
        {
            x: 50,
            y: 180,
            value: json[3].MediaMinuto,
            radius: 50,
        },
        {
            x: 130,
            y: 180,
            value: json[4].MediaMinuto,
            radius: 55,
        },
        {
            x: 220,
            y: 180,
            value: json[5].MediaMinuto,
            radius: 65,
        },
        {
            x: 330,
            y: 200,
            value: json[6].MediaMinuto,
            radius: 65,
        },
        {
            x: 97,
            y: 290,
            value: json[7].MediaMinuto,
            radius: 20,
        },
        {
            x: 140,
            y: 290,
            value: json[8].MediaMinuto,
            radius: 20,
        },
        {
            x: 183,
            y: 290,
            value: json[9].MediaMinuto,
            radius: 20,
        },
        {
            x: 227,
            y: 290,
            value: json[10].MediaMinuto,
            radius: 20,
        },
        {
            x: 270,
            y: 290,
            value: json[11].MediaMinuto,
            radius: 20,
        }
    ];


    points = points.concat(locais);

    // formato para gerar mapa
    var data = {
        max: max,
        min: min,
        data: points,
    };

    // Inicia pontos no mapa de calor
    heatmapInstance.setData(data);

};

var randomScalingFactor = function () {
    return Math.round(Math.random() * 100);
};

var randomData = function () {
    return [
        15, 33, 70, 85, 100
    ];
};

let data = randomData();

//Config. do primeiro gráfico de linha
var dados = {
    labels: [],
    datasets: [{
            yAxisID: 'y-media',
            label: 'Media de Movimentação/Min',
            borderColor: window.chartColors.red,
            backgroundColor: window.chartColors.red,
            fill: false,
            data: []
        },

    ]
};


// só mexer se quiser alterar o tempo de atualização
// ou se souber o que está fazendo!


// altere aqui como os dados serão exibidos
// e como são recuperados do BackEnd
function obterDadosGraficoLinha() {

    fetch(`/dado/ultimas/${setorCB}`, {
            cache: 'no-store'
        }).then(function (response) {
            if (response.ok) {
                response.json().then(function (resposta) {

                    console.log(`Dados recebidos: ${JSON.stringify(resposta)}`);

                    resposta.reverse();
                    dados.labels.shift();
                    dados.labels.shift();
                    dados.labels.shift();
                    dados.labels.shift();
                    dados.labels.shift();
                    dados.labels.shift();
                    dados.datasets[0].data.shift();
                    dados.datasets[0].data.shift();
                    dados.datasets[0].data.shift();
                    dados.datasets[0].data.shift();
                    dados.datasets[0].data.shift();
                    dados.datasets[0].data.shift();

                    for (i = 0; i < resposta.length; i++) {
                        var registro = resposta[i];



                        // aqui, após 'registro.' use os nomes 
                        // dos atributos que vem no JSON 
                        // que gerou na consulta ao banco de dados
                        let horario = registro.Horario.split('T')[1].split('.')[0];

                        dados.labels.push(horario);

                        dados.datasets[0].data.push(registro.MediaMinuto.toFixed(1));
                    }
                    plotarGrafico(dados);

                    //console.log(JSON.stringify(dados));

                    div_aguarde.style.display = 'none';


                });
            } else {
                console.error('Nenhum dado encontrado ou erro na API');
            }
        })
        .catch(function (error) {
            console.error(`Erro na obtenção dos dados p/ gráfico: ${error.message}`);
        });

}



// só altere aqui se souber o que está fazendo!
function plotarGrafico(dados) {
    console.log('iniciando plotagem do gráfico...');

    var ctx = canvas_grafico_linha1.getContext('2d');
    window.grafico_linha = Chart.Line(ctx, {
        data: dados,
        options: configurarGrafico()
    });

    window.grafico_linha.update();
}

function configurarGrafico() {
    var configuracoes = {
        responsive: true,
        animation: {
            duration: 500
        },
        hoverMode: 'index',
        stacked: false,
        title: {
            display: true,
            text: 'Histórico recente de fluxo de clientes'
        },
        scales: {
            yAxes: [{
                type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                display: true,
                position: 'left',
                id: 'y-media',
            }],
        }
    };

    return configuracoes;
}

function buscarPresencasTempo() {
    //var formulario = new URLSearchParams(new FormData(heatmap_form));

    const diaFiltro = document.getElementById('dia').value;
    const horaIniFiltro = document.getElementById('hora_ini').value;
    const horaFimFiltro = document.getElementById('hora_fim').value;


    console.log(diaFiltro)
    console.log(horaFimFiltro)
    console.log(horaIniFiltro)
    

    // Configuração minima, container padrão
    fetch("/dado/presenca-hora", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: "POST",
        body:  JSON.stringify({
            dia: diaFiltro,
            hora_ini: horaIniFiltro,
            hora_fim: horaFimFiltro
        }),
    }).then((resposta) => {
        if (resposta.ok) {
            resposta.json().then((json) => {
                console.log("JSON AQUI", json);
                

                var points = [];
                var max = 100;
                var min = 0;
                var width = 850;
                var height = 490;

                heatmapInstance.setData({
                    data: []
                });


                //Gerando um ponto por local da planta
                const locais = [{
                        x: 60,
                        y: 60,
                        value: 0,
                        radius: 70,
                    },
                    {
                        x: 200,
                        y: 60,
                        value: 0,
                        radius: 60,
                    },
                    {
                        x: 340,
                        y: 60,
                        value: 0,
                        radius: 70,
                    },
                    {
                        x: 50,
                        y: 180,
                        value: 0,
                        radius: 50,
                    },
                    {
                        x: 130,
                        y: 180,
                        value: 0,
                        radius: 55,
                    },
                    {
                        x: 220,
                        y: 180,
                        value: 0,
                        radius: 65,
                    },
                    {
                        x: 330,
                        y: 200,
                        value: 0,
                        radius: 65,
                    },
                    {
                        x: 97,
                        y: 290,
                        value: 0,
                        radius: 20,
                    },
                    {
                        x: 140,
                        y: 290,
                        value: 0,
                        radius: 20,
                    },
                    {
                        x: 183,
                        y: 290,
                        value: 0,
                        radius: 20,
                    },
                    {
                        x: 227,
                        y: 290,
                        value: 0,
                        radius: 20,
                    },
                    {
                        x: 270,
                        y: 290,
                        value: 0,
                        radius: 20,
                    }
                ];

                console.log(json[i])
                // for (let i = 0; i < locais.length; i++) {
                //     locais[i].value = json[i].media
                // };

                points = points.concat(locais);

                // formato para gerar mapa
                var data = {
                    max: max,
                    min: min,
                    data: points,
                };
                console.log(data);
                // Inicia pontos no mapa de calor
                heatmapInstanceTempo.setData(data);
            });
        } else {
            console.log("Erro ao buscar quantidade de presença!");

            resposta.text().then((texto) => {
                console.error(texto);
            });
        }
    });
    return false;
}

//Todos os configs pros gauges
const config = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config2 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config3 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config4 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config5 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config6 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config7 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config8 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config9 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config10 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config11 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};
const config12 = {
    type: 'gauge',
    data: {
        labels: ["Fraco", "Alerta", "Ideal", "Alerta", "Crítico"],
        datasets: [{
            data: data,
            value: 0,
            backgroundColor: ['#729fcf', 'yellow', '#069a2e', 'orange', 'red'],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Setor'
        },
        layout: {
            padding: {
                bottom: 30
            }
        },
        needle: {
            // Needle circle radius as the percentage of the chart area width
            radiusPercentage: 2,
            // Needle width as the percentage of the chart area width
            widthPercentage: 3.2,
            // Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
            lengthPercentage: 80,
            // The color of the needle
            color: 'rgba(0, 0, 0, 1)'
        },
        valueLabel: {
            display: true,
            formatter: (value) => {
                return Math.round(value) + '%';
            }
        },
        plugins: {
            datalabels: {
                display: true,
                formatter: function (value, context) {
                    return context.chart.data.labels[context.dataIndex];
                },
                //color: function (context) {
                //  return context.dataset.backgroundColor;
                //},
                color: 'rgba(0, 0, 0, 1.0)',
                //color: 'rgba(255, 255, 255, 1.0)',
                backgroundColor: null,
                font: {
                    size: 14,
                    weight: 'bold'
                }
            }
        }
    }
};




window.onload = function () {
    obterDadosGraficoLinha();
    var ctx = document.getElementById('gauge1').getContext('2d');
    var ctx2 = document.getElementById('gauge2').getContext('2d');
    var ctx3 = document.getElementById('gauge3').getContext('2d');
    var ctx4 = document.getElementById('gauge4').getContext('2d');
    var ctx5 = document.getElementById('gauge5').getContext('2d');
    var ctx6 = document.getElementById('gauge6').getContext('2d');
    var ctx7 = document.getElementById('gauge7').getContext('2d');
    var ctx8 = document.getElementById('gauge8').getContext('2d');
    var ctx9 = document.getElementById('gauge9').getContext('2d');
    var ctx10 = document.getElementById('gauge10').getContext('2d');
    var ctx11 = document.getElementById('gauge11').getContext('2d');
    var ctx12 = document.getElementById('gauge12').getContext('2d');
    window.myGauge0 = new Chart(ctx, config);
    window.myGauge1 = new Chart(ctx2, config2);
    window.myGauge2 = new Chart(ctx3, config3);
    window.myGauge3 = new Chart(ctx4, config4);
    window.myGauge4 = new Chart(ctx5, config5);
    window.myGauge5 = new Chart(ctx6, config6);
    window.myGauge6 = new Chart(ctx7, config7);
    window.myGauge7 = new Chart(ctx8, config8);
    window.myGauge8 = new Chart(ctx9, config9);
    window.myGauge9 = new Chart(ctx10, config10);
    window.myGauge10 = new Chart(ctx11, config11);
    window.myGauge11 = new Chart(ctx12, config12);
    atualizarGrafico();
    verificar_autenticacao();
};

fetch('/setor/1', {
    cache: 'no-store'
}).then(function (response) {
    if (response.ok) {
        response.json().then(function (resposta) {
            for (let index = 0; index < resposta.length; index++) {
                setor_cb.innerHTML += `<option value='${resposta[index].idSetor}'>${resposta[index].nome}</option>`;

            }
            window.myGauge0.config.options.title.text = resposta[0].nome;
            window.myGauge1.config.options.title.text = resposta[1].nome;
            window.myGauge2.config.options.title.text = resposta[2].nome;
            window.myGauge3.config.options.title.text = resposta[3].nome;
            window.myGauge4.config.options.title.text = resposta[4].nome;
            window.myGauge5.config.options.title.text = resposta[5].nome;
            window.myGauge6.config.options.title.text = resposta[6].nome;
            window.myGauge7.config.options.title.text = resposta[7].nome;
            window.myGauge8.config.options.title.text = resposta[8].nome;
            window.myGauge9.config.options.title.text = resposta[9].nome;
            window.myGauge10.config.options.title.text = resposta[10].nome;
            window.myGauge11.config.options.title.text = resposta[11].nome;
            window.myGauge0.update();
            window.myGauge1.update();
            window.myGauge2.update();
            window.myGauge3.update();
            window.myGauge4.update();
            window.myGauge5.update();
            window.myGauge6.update();
            window.myGauge7.update();
            window.myGauge8.update();
            window.myGauge9.update();
            window.myGauge10.update();
            window.myGauge11.update();
        });
    }
});

function atualizarGrafico() {
    obterDadosGrafico();
    setTimeout(atualizarGrafico, 5000);
}

function obterDadosGrafico() {
    var dados;

    fetch('/dado/gauge-tempo-real', {
            cache: 'no-store'
        }).then(function (response) {
            if (response.ok) {
                response.json().then(function (resposta) {

                    console.log(`Dados recebidos: ${JSON.stringify(resposta)}`);
                    buscarPresencas(resposta);
                    window.myGauge0.config.data.datasets[0].value = resposta[0].MediaMinuto;
                    window.myGauge1.config.data.datasets[0].value = resposta[1].MediaMinuto;
                    window.myGauge2.config.data.datasets[0].value = resposta[2].MediaMinuto;
                    window.myGauge3.config.data.datasets[0].value = resposta[3].MediaMinuto;
                    window.myGauge4.config.data.datasets[0].value = resposta[4].MediaMinuto;
                    window.myGauge5.config.data.datasets[0].value = resposta[5].MediaMinuto;
                    window.myGauge6.config.data.datasets[0].value = resposta[6].MediaMinuto;
                    window.myGauge7.config.data.datasets[0].value = resposta[7].MediaMinuto;
                    window.myGauge8.config.data.datasets[0].value = resposta[8].MediaMinuto;
                    window.myGauge9.config.data.datasets[0].value = resposta[9].MediaMinuto;
                    window.myGauge10.config.data.datasets[0].value = resposta[10].MediaMinuto;
                    window.myGauge11.config.data.datasets[0].value = resposta[11].MediaMinuto;
                    window.myGauge0.update();
                    window.myGauge1.update();
                    window.myGauge2.update();
                    window.myGauge3.update();
                    window.myGauge4.update();
                    window.myGauge5.update();
                    window.myGauge6.update();
                    window.myGauge7.update();
                    window.myGauge8.update();
                    window.myGauge9.update();
                    window.myGauge10.update();
                    window.myGauge11.update();





                    // aqui, após registro. use os nomes 
                    // dos atributos que vem no JSON 
                    // que gerou na consulta ao banco de dados

                    // dadosTemperatura = google.visualization.arrayToDataTable([
                    //     ['Label', 'Value'],
                    //     ['Temperatura', resposta.temperatura]
                    // ]);

                    // dadosUmidade = google.visualization.arrayToDataTable([
                    //     ['Label', 'Value'],
                    //     ['Umidade', resposta.umidade]
                    // ]);

                    // var dados = {
                    //     temperatura: dadosTemperatura,
                    //     umidade: dadosUmidade
                    // }

                    // alertar(resposta.temperatura, resposta.umidade);
                    // plotarGrafico(dados);
                });
            } else {
                console.error('Nenhum dado encontrado ou erro na API');
            }
        })
        .catch(function (error) {
            console.error(`Erro na obtenção dos dados p/ gráfico: ${error.message}`);
        });

}

verificar_autenticacao();