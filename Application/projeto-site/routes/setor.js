var express = require('express');
var router = express.Router();
var sequelize = require('../models').sequelize;
var Setor = require('../models').Setor;

router.get('/:idFilial', function (req, res, next) {
        const idFilial = req.params.idFilial;
        console.log(`Recuperando todos os setores da filial ${idFilial}`);
        const instrucaoSql = `SELECT * FROM Setor WHERE fkFilial = ${idFilial};`;


        sequelize.query(instrucaoSql, { type: sequelize.QueryTypes.SELECT })
                .then(resultado => {
                        res.json(resultado);
                }).catch(erro => {
                        console.error(erro)
                        res.status(500).send(erro.message);
                });
});
router.get('/all/:idSetor', function (req, res, next) {
        const idSetor = req.params.idSetor;
        console.log(`Recuperando todos os dados do Setor ${idSetor}`);
        const instrucaoSql = `SELECT * FROM Setor WHERE idSetor = ${idSetor};`;


        sequelize.query(instrucaoSql, { type: sequelize.QueryTypes.SELECT })
                .then(resultado => {
                        res.json(resultado);
                }).catch(erro => {
                        console.error(erro)
                        res.status(500).send(erro.message);
                });
});

// Editar setor
router.post('/editar/:idSetor', function (req, res, next) {
        console.log('Editando o setor');
        var { nomeSetor } = req.body;
        var { qtdSensores } = req.body;
        var { idSetor } = req.params;
        console.log(nomeSetor, qtdSensores);

        let instrucaoSql = `UPDATE setor SET nome = '${nomeSetor}', qtdSensores = ${qtdSensores} WHERE idSetor = '${idSetor}';`;

        sequelize.query(instrucaoSql).then(resultado => {
                console.log(`Setor editado: ${resultado}`)
                res.json({ message: "Atualizado com sucesso" })
        }).catch(erro => {
                console.error(erro);
                res.status(500).send(erro.message);
        });
});


module.exports = router;
