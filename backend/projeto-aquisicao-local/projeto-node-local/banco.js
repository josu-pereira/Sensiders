var configuracoes = {
    banco: {
        server: "serversendiers.database.windows.net",
        user: "201grupo11c@bandtec.com.br",
        password: "#Gfgrupo11c",
        database: "bdProjetoSensiders",
        options: {
            encrypt: true
        },
        pool: {
            max: 4,
            min: 1,
            idleTimeoutMillis: 30000,
            connectionTimeout: 5000
        }
    }
}
 
var sql = require('mssql');
sql.on('error', err => {
    console.error(`Erro de Conexão: ${err}`);
});


function conectar() {
  sql.close();
  return sql.connect(configuracoes.banco)
} 

module.exports = {
    conectar: conectar,
    sql: sql
}
