package model.dao;

import connection.Connection;
import model.bean.Componente;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import java.util.*;

public class ComponenteDAO {
    
    
    public void insertComponente(Componente comp) {
        
        try {
            System.out.println(comp.getNomeComponente());
            System.out.println(comp.getTotalComponente());
            System.out.println(comp.getMetricaComponente());
            System.out.println(comp.getMedidaAlertaComponente());
          
            Connection conn = new Connection();
            JdbcTemplate jdbcTemplate = conn.getConnection();
            
            jdbcTemplate.query("INSERT INTO Componente(nomeComponente, totalComponente, metricaComponente, medidaAlertaComponente) VALUES(?, ?, ?, ?)", 
                    new BeanPropertyRowMapper(Componente.class), comp.getNomeComponente(),
                    comp.getTotalComponente(), comp.getMetricaComponente(), comp.getMedidaAlertaComponente());
        
           
        } catch (DataAccessException e) {
            System.out.println("Deu erro: " + e.getMessage());
            
        }
    }
    
}
