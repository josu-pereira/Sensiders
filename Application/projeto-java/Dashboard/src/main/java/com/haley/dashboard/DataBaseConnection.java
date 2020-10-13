package com.haley.dashboard;

import java.util.List;
import java.util.Scanner;
import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;


public class DataBaseConnection {

     public static void main(String[] args) {
        
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
        dataSource.setUrl("jdbc:sqlserver://serversensiders.database.windows.net:1433;"
                + "database=bdProjetoSensiders;encrypt=true;trustServerCertificate=false;"
                + "hostNameInCertificate=*.database.windows.net;loginTimeout=30;");
        dataSource.setUsername("adminlocal");
        dataSource.setPassword("#Gfgrupo11c");
        
        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
        
        List<Users> listaUsuarios = jdbcTemplate.query("select * from Usuario", new BeanPropertyRowMapper(Users.class));
        
//        return listaUsuarios;
                //         System.out.println(listaUsuarios);
//            for (Users dado : listaUsuarios) {
//                System.out.println(dado.getNomeUsuario());
//            }
     }
    
}
