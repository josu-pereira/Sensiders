/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import java.util.Map;
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
            
            List<Componente> componentes;
            componentes = jdbc.query("select idComponente, nomeComponente, totalComponente, "
                    + "metricaComponente, medidaAlertaComponente from vwListaComponentes\n" +
                    "where idMaquina = ?", 
                    new BeanPropertyRowMapper(Componente.class), maquina);
            
            return componentes;
            
        } catch (DataAccessException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }
    
    public Double returnLeitura(Integer filial, Integer componente, Integer maquina){
        try {
            Connection conn = new Connection();
            JdbcTemplate jdbc = conn.getConnection();
            Double leitura = 0.0;
            
            List<Map<String, Object>> aux = jdbc.queryForList("select componentes = dbo.fc_returnLeitura(?, ?, ?)", filial, componente, maquina);
            
            leitura = Double.valueOf(aux.get(0).get("componentes").toString());
            
            return leitura;
        } catch (DataAccessException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }
    
}
