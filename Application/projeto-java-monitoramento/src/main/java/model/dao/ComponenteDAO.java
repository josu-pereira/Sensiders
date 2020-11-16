/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import model.bean.Componente;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author Patrick L Teixeira
 */
public class ComponenteDAO {
    
    public List<Componente> returnComponentes(Integer maquina){
        try {
            Connection conn = new Connection();
            JdbcTemplate jdbc = conn.getConnection();
            
            List<Componente> componentes = jdbc.query("SELECT * FROM vwListaComponentes where idMaquina = ?", 
                    new BeanPropertyRowMapper(Componente.class), maquina);
            
            return componentes;
            
        } catch (DataAccessException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }
    
}
