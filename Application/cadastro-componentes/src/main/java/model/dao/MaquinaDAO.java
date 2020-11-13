/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import model.bean.Componente;
import model.bean.Maquina;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

public class MaquinaDAO {
    
    
    public List<Maquina> selectComponente(int idFilial) {
        try {
           
            Connection conn = new Connection();
            JdbcTemplate jdbcTemplate = conn.getConnection();
            Maquina setor = new Maquina();
            
            
            List<Maquina> listMaquinas = jdbcTemplate.query("SELECT * FROM maquina where fkFilial = ?", 
                    new BeanPropertyRowMapper(Maquina.class), idFilial);
            
            
            listMaquinas.forEach(s -> {
                setor.setIdMaquina(s.getIdMaquina());
                setor.setFkFilial(s.getFkFilial());
                setor.setDescricaoMaquina(s.getDescricaoMaquina());
                setor.setHashmac(s.getHashmac());
            
            });
            
            return listMaquinas;
        } catch (DataAccessException e) {
            System.out.println("DEU ERRO: "+e.getMessage());
            return null;
        }
    }
}
