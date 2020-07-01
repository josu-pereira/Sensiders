'use strict';

/* 
lista e explicação dos Datatypes:
https://codewithhugo.com/sequelize-data-types-a-practical-guide/
*/

module.exports = (sequelize, DataTypes) => {
    let Supermercado = sequelize.define('Supermercado',{
		id: {
			field: 'idSupermercado',
			type: DataTypes.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},		
		nome: {
			field: 'nome',
			type: DataTypes.STRING,
			allowNull: false
		},
	}, 
	{
		tableName: 'Supermercado', 
		freezeTableName: true, 
		underscored: true,
		timestamps: false,
	});

    return Supermercado;
};
