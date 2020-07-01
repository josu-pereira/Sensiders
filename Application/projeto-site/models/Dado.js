'use strict';

/* 
lista e explicação dos Datatypes:
https://codewithhugo.com/sequelize-data-types-a-practical-guide/
*/

module.exports = (sequelize, DataTypes) => {
    let Dado = sequelize.define('Dado',{
		dataHora: {
			field: 'dataHora',
			type: DataTypes.DATE,
			primaryKey: true
		},
        fkSetor: {
            field: 'fkSetor',
            type: DataTypes.INTEGER,
            references: {
                model: 'Setor',
                key: 'idSetor',
            },
            primaryKey: true,
        },
        grauMov: {
            field: 'grauMov',
            type: DataTypes.DECIMAL(4,1),
            allowNull: false,
        }
	}, 
	{
		tableName: 'Dado', 
		freezeTableName: true, 
		underscored: true,
		timestamps: false,
	});

    return Dado;
};
