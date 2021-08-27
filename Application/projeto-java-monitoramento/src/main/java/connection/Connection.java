/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package connection;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author Patrick L Teixeira
 */
public class Connection {
    
    /*
    credenciais MYSQL: 
        DRIVER = "com.mysql.jdbc.Driver";
        URL = "jdbc:mysql://3.93.53.111:3306/bdProjetoSensiders?useTimezone=true&serverTimezone=UTC";
        USERNAME = "root"
        PASSWORD = "urubu100"
    
    credencias AZURE:
        DRIVER = "com.microsoft.sqlserver.jdbc.SQLServerDriver";
        URL = "jdbc:sqlserver://serversensiders.database.windows.net:1433;"
        USERNAME = "adminlocal";
        PASSWORD = "#Gfgrupo11c";
    */
    
    private static final String  DRIVER = "com.mysql.jdbc.Driver";
    private static final String URL = "jdbc:mysql://3.93.53.111:3306/bdProjetoSensiders?useTimezone=true&serverTimezone=UTC";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "urubu100";
    
    public static JdbcTemplate getConnection(){
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName(DRIVER);
        dataSource.setUrl(URL);
        dataSource.setUsername(USERNAME);
        dataSource.setPassword(PASSWORD);
        
        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
        return jdbcTemplate;
    }
}
