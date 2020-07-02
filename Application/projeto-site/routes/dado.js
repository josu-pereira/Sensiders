var express = require('express');
var router = express.Router();
var sequelize = require('../models').sequelize;
var Dado = require('../models').Dado;

// Recuperar as ultimas n leituras
router.post('/presenca-hora', function(req, res, next) {
	
	// quantas são as últimas leituras que quer? 8 está bom?
	var dia = req.body.dia;
	var hora_ini = req.body.hora_ini;
	var hora_fim = req.body.hora_fim;

	console.log(`Hora inicio: ${hora_ini}`);
	console.log(`Hora fim: ${hora_fim}`);
	
	const instrucaoSql = `SELECT round(avg(grauMov), 1) as media, fkSetor
	FROM dado, setor 
	WHERE fkSetor = idSetor
	AND dataHora >= '${dia}T${hora_ini}:00' and dataHora <= '${dia}T${hora_fim}:00'
	GROUP BY fkSetor ORDER BY fkSetor;`;

	sequelize.query(instrucaoSql, {
		model: Dado,
		mapToModel: true 
	  })
	  .then(resultado => {
			console.log(`Encontrados: ${resultado.length}`);
			res.json(resultado);
	  }).catch(erro => {
			console.error(erro);
			res.status(500).send(erro.message);
	  });
});

/* Recuperar as últimas N leituras */
router.get('/ultimas/:idSetor', function (req, res, next) {
	const idSetor = req.params.idSetor;
	// quantas são as últimas leituras que quer? 8 está bom?
	const limite_linhas = 6;

	console.log(`Recuperando as últimas ${limite_linhas} leituras`);
	let agora = new Date().getTime();
	let instrucaoSql = '';
	for (let index = 1; index <= limite_linhas; index++) {
		const time = new Date(agora);
		const timeBefore = new Date(agora - 1000 * 60);
		instrucaoSql += `SELECT fkSetor, min(dataHora) as 'Horario', avg(grauMov) as 'MediaMinuto' from dado where (dataHora >= ('2020-${adicionarZero( timeBefore.getMonth() + 1)}-${adicionarZero( timeBefore.getDate())}T${adicionarZero( timeBefore.getHours())}:${adicionarZero( timeBefore.getMinutes())}:00') and (dataHora < '2020-${adicionarZero( time.getMonth() + 1)}-${adicionarZero( time.getDate())}T${adicionarZero( time.getHours())}:${adicionarZero( time.getMinutes())}:00')) and fkSetor = ${idSetor} group by fkSetor`;
		agora = timeBefore;
		if (index == limite_linhas) {
			instrucaoSql += ';';
		}
		else {
			instrucaoSql += ' union all '; 
		}
	}



	sequelize.query(instrucaoSql, {
		model: Dado,
		mapToModel: true
	})
		.then(resultado => {
			console.log(`Encontrados: ${resultado.length}`);
			res.json(resultado);
		}).catch(erro => {
			console.error(erro);
			res.status(500).send(erro.message);
		});
});

// tempo real (último valor de cada leitura)
router.get('/ultima-media/:idSetor', function (req, res, next) {

	const idSetor = req.params.idSetor;

	console.log(`Recuperando a última leitura`);
	const time = new Date();
	const timeBefore = new Date(time.getTime() - 1000 * 60);
	const instrucaoSql = `SELECT top 1 fkSetor, min(dataHora) as 'Horario', avg(grauMov) as 'MediaMinuto' from dado where (dataHora >= ('2020-${adicionarZero( timeBefore.getMonth() + 1)}-${adicionarZero( timeBefore.getDate())}T${adicionarZero( timeBefore.getHours())}:${adicionarZero( timeBefore.getMinutes())}:00') and (dataHora < '2020-${adicionarZero( time.getMonth() + 1)}-${adicionarZero( time.getDate())}T${adicionarZero( time.getHours())}:${adicionarZero( time.getMinutes())}:00')) and fkSetor = ${idSetor} group by fkSetor`;

	sequelize.query(instrucaoSql, { type: sequelize.QueryTypes.SELECT })
		.then(resultado => {
			res.json(resultado[0]);
		}).catch(erro => {
			console.error(erro);
			res.status(500).send(erro.message);
		});

});

router.get('/tempo-real', function (req, res, next) {

	console.log(`Recuperando a última leitura`);
	const instrucaoSql = 'SELECT top 1 grauMov from dado where fkSetor = 1 order by dataHora desc';

	sequelize.query(instrucaoSql, { type: sequelize.QueryTypes.SELECT })
		.then(resultado => {
			res.json(resultado[0]);
		}).catch(erro => {
			console.error(erro);
			res.status(500).send(erro.message);
		});

});

//Pegar os últimos dados inseridos em cada setor

router.get('/gauge-tempo-real', function (req, res, next) {
	console.log('Recuperando as últimas leituras');
	const instrucaoSql = "SELECT TOP 12 fkSetor,Setor.nome, dataHora AS 'Horario', grauMov AS 'MediaMinuto' FROM dado INNER JOIN Setor ON idSetor = fkSetor INNER JOIN Filial ON idFilial = fkFilial WHERE fkFilial = 1 ORDER BY dataHora DESC;";
	
	sequelize.query(instrucaoSql, {type: sequelize.QueryTypes.SELECT })
		.then(resultado => {
			res.json(resultado);
		}).catch(erro => {
			console.error(erro)
			res.status(500).send(erro.message);
		});
});

// estatísticas (max, min, média, mediana, quartis etc)
router.get('/estatisticas', function (req, res, next) {

	console.log(`Recuperando as estatísticas atuais`);

	const instrucaoSql = `select 
							max(temperatura) as temp_maxima, 
							min(temperatura) as temp_minima, 
							avg(temperatura) as temp_media,
							max(umidade) as umidade_maxima, 
							min(umidade) as umidade_minima, 
							avg(umidade) as umidade_media 
						from leitura`;

	sequelize.query(instrucaoSql, { type: sequelize.QueryTypes.SELECT })
		.then(resultado => {
			res.json(resultado[0]);
		}).catch(erro => {
			console.error(erro);
			res.status(500).send(erro.message);
		});

});

function adicionarZero(numero) {
	if(numero < 10) {
	  return `0${numero}`;
	}
	else return numero;
  }

module.exports = router;
