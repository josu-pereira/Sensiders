var express = require('express');
const { Sequelize } = require('../models');
var router = express.Router();
var sequelize = require('../models').sequelize;
var Usuario = require('../models').Usuario;
var Supermercado = require('../models').Supermercado;
const sendEmail = require("./../config/email");

let sessoes = [];

/* Recuperar usuário por login e senha */
router.post('/autenticar', function(req, res, next) {
	console.log('Recuperando usuário por login e senha');

	var login = req.body.login; // depois de .body, use o nome (name) do campo em seu formulário de login
	var senha = req.body.senha; // depois de .body, use o nome (name) do campo em seu formulário de login	
	
	let instrucaoSql = `select * from Usuario where emailUsuario='${login}' and senhaUsuario='${senha}'`;
	console.log(instrucaoSql);

	sequelize.query(instrucaoSql, {
		model: Usuario
	}).then(resultado => {
		console.log(`Encontrados: ${resultado.length}`);

		if (resultado.length == 1) {
			// console.log(resultado[0].dataValues);
			sessoes.push(resultado[0].dataValues.emailUsuario);
			console.log('sessoes: ',sessoes);
			res.json(resultado[0]);
		} else if (resultado.length == 0) {
			res.status(403).send('Login e/ou senha inválido(s)');
		} else {
			res.status(403).send('Mais de um usuário com o mesmo login e senha!');
		}

	}).catch(erro => {
		console.error(erro);
		res.status(500).send(erro.message);
  	});
});

/* Cadastrar usuário */
router.post('/cadastrar', function(req, res, next) {
	console.log('Criando um usuário');
	
	const mercado = req.body.mercado;
	const cep = req.body.cep;
	const numero = req.body.numero;
	const nome = req.body.nome;
	const email = req.body.email;
	const senha = req.body.senha;

	let instrucaoSql = `EXEC sp_NovoUsuario '${mercado}', '${cep}', ${numero}, '${nome}','${email}','${senha}'; `;

	sequelize.query(instrucaoSql).then(resultado => {
		console.log(`Registro criado: ${resultado}`)
        res.send(resultado);
    }).catch(erro => {
		console.error(erro);
		res.status(500).send(erro.message);
  	});
});


/* Verificação de usuário */
router.get('/sessao/:login', function(req, res, next) {
	let login = req.params.login;
	console.log(`Verificando se o usuário ${login} tem sessão`);
	
	let tem_sessao = false;
	for (let u=0; u<sessoes.length; u++) {
		if (sessoes[u] == login) {
			tem_sessao = true;
			break;
		}
	}

	if (tem_sessao) {
		let mensagem = `Usuário ${login} possui sessão ativa!`;
		console.log(mensagem);
		res.send(mensagem);
	} else {
		res.sendStatus(403);
	}
	
});


/* Logoff de usuário */
router.get('/sair/:login', function(req, res, next) {
	let login = req.params.login;
	console.log(`Finalizando a sessão do usuário ${login}`);
	let nova_sessoes = []
	for (let u=0; u<sessoes.length; u++) {
		if (sessoes[u] != login) {
			nova_sessoes.push(sessoes[u]);
		}
	}
	sessoes = nova_sessoes;
	res.send(`Sessão do usuário ${login} finalizada com sucesso!`);
});

/*rota do email*/ 
router.post('/recuperarSenha', function(req, res){
	const {email} = req.body;

	let sql = `SELECT senhaUsuario, nomeUsuario FROM Usuario where emailUsuario = '${email}'`
	sequelize.query(sql, {
		model: Usuario
	}).then(resultado => {
		if(resultado.length == 1){
			let nome = resultado[0].dataValues.nomeUsuario;
			let senha = resultado[0].dataValues.senhaUsuario;
			const bodyEmailUser = {
				from: "201grupo11c@bandtec.com.br",
				to :email,
				subject: "Recuperar senha",	
				text: `Ola ${nome}, parece que você esqueceu sua senha, mas estamos aqui para te lembrar! Senha: ${senha}`
			};
		
			sendEmail.sendMail(bodyEmailUser, (err)=>{
				if(err) console.log(err)
				res.json({
					"response": "Email enviado"
				});
				console.log("email enviado")
				console.log(resultado[0].dataValues.senhaUsuario);
			});
		}else if(resultado.length == 0){
			res.status(403).send('email inválido(s)');
		}else{
			res.status(403).send('existe mais de um email igual a este');
		}

	})
	console.log(email)
});


/* Recuperar todos os usuários */
router.get('/', function(req, res, next) {
	console.log('Recuperando todos os usuários');
	Usuario.findAndCountAll().then(resultado => {
		console.log(`${resultado.count} registros`);

		res.json(resultado.rows);
	}).catch(erro => {
		console.error(erro);
		res.status(500).send(erro.message);
  	});
});

module.exports = router;
