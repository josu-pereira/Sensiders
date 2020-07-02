var express = require('express');
var router = express.Router();
var sequelize = require('../models').sequelize;
var Setor = require('../models').Setor;

router.get('/:idFilial', function (req, res, next) {
	const idFilial = req.params.idFilial;
        console.log(`Recuperando todos os setores da filial ${idFilial}`);
        const instrucaoSql = `SELECT * FROM Setor WHERE fkFilial = ${idFilial};`;

        sequelize.query(instrucaoSql, {type: sequelize.QueryTypes.SELECT })
                .then(resultado => {
                        res.json(resultado);
                }).catch(erro => {
                        console.error(erro)
                        res.status(500).send(erro.message);
                });
});

module.exports = router;
