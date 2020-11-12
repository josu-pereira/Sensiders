/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import model.bean.Maquina;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author Patrick L Teixeira
 */
public class MaquinaDAO {
    
    public List<Maquina> returnMaquinas(Integer fkFilial){
        try {
            Connection conn = new Connection();
            JdbcTemplate jdbc = conn.getConnection();
            
            List<Maquina> maquinas = jdbc.query("SELECT * FROM MAQUINA WHERE fkFilial = ?", 
                    new BeanPropertyRowMapper(Maquina.class), fkFilial);
            
            return maquinas;
        } catch (DataAccessException e) {
            return null;
        }
    }
    
}
