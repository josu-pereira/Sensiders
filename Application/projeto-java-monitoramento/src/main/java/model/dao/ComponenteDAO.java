/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import model.bean.Componente;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author Patrick L Teixeira
 */
public class ComponenteDAO {
    
    public List<Componente> returnComponentes(Integer idMaquina){
        try {
            Connection conn = new Connection();
            JdbcTemplate jdbc = conn.getConnection();
            
            
        } catch (Exception e) {
        }
    }
    
}
