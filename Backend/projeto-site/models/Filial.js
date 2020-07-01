'use strict';

/* 
lista e explicação dos Datatypes:
https://codewithhugo.com/sequelize-data-types-a-practical-guide/
*/

module.exports = (sequelize, DataTypes) => {
    let Filial = sequelize.define('Filial',{
		id: {
			field: 'idFilial',
			type: DataTypes.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},		
		cep: {
			field: 'cep',
			type: DataTypes.CHAR,
			allowNull: false
        },
        numero: {
            field: 'numero',
            type: DataTypes.INTEGER,
            allowNull: false
        },
        fkSupermercado: {
            field: 'fkSupermercado',
            type: DataTypes.INTEGER,
            allowNull: false,
            references: {
                model: 'Supermercado',
                key: 'idSupermercado',
            }
        },
	}, 
	{
		tableName: 'Filial', 
		freezeTableName: true, 
		underscored: true,
		timestamps: false,
	});

    return Filial;
};
