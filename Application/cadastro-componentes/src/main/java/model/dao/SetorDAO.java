/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import model.bean.Componente;
import model.bean.Setor;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

public class SetorDAO {
    
    
    public List<Setor> selectComponente(int idFilial) {
        try {
           
            Connection conn = new Connection();
            JdbcTemplate jdbcTemplate = conn.getConnection();
            Setor setor = new Setor();
            
            
            List<Setor> listaSetores = jdbcTemplate.query(
                    "SELECT * FROM setor where fkFilial = ?", 
                    new BeanPropertyRowMapper(Setor.class), idFilial);
            
            
            listaSetores.forEach(s -> {
                setor.setIdSetor(s.getIdSetor());
                setor.setFkFilial(s.getFkFilial());
                setor.setNome(s.getNome());
                setor.setQtdSensores(s.getQtdSensores());
            
            });
            
            return listaSetores;
        } catch (DataAccessException e) {
            System.out.println("DEU ERRO: "+e.getMessage());
            return null;
        }
    }
}
