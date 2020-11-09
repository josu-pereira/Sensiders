package connection;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class Connection {
    private final String Driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver";
    private final String URL = "jdbc:sqlserver://serversensiders.database.windows.net:1433;"
            + "database=bdProjetoSensiders;encrypt=true;trustServerCertificate=false;"
            + "hostNameInCertificate=*.database.windows.net;loginTimeout=30";
    private final String USERNAME = "adminlocal";
    private final String PASSWORD = "#Gfgrupo11c";
    
    public JdbcTemplate getConnection() {
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName(Driver);
        dataSource.setUrl(URL);
        dataSource.setUsername(USERNAME);
        dataSource.setPassword(PASSWORD);
        
        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
        return jdbcTemplate;
    }
}
