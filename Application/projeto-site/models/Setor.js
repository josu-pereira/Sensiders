'use strict';

/* 
lista e explicação dos Datatypes:
https://codewithhugo.com/sequelize-data-types-a-practical-guide/
*/

module.exports = (sequelize, DataTypes) => {
    let Setor = sequelize.define('Setor',{
		id: {
			field: 'idSetor',
			type: DataTypes.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},		
		nome: {
			field: 'nome',
			type: DataTypes.STRING,
			allowNull: false
		},
		qtdSensores: {
			field: 'qtdSensores',
			type: DataTypes.INTEGER,
			allowNull: false
		},
		fkFilial: {
			field: 'fkFilial',
			type: DataTypes.INTEGER,
            allowNull: false,
			references: {
                model: 'Filial',
                key: 'idFilial',
			}
		},
	}, 
	{
		tableName: 'Setor', 
		freezeTableName: true, 
		underscored: true,
		timestamps: false,
	});

    return Setor;
};
