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
    
    public static List<Componente> returnComponentes(Integer maquina){
        try {
            JdbcTemplate jdbc = Connection.getConnection();         
            
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
    
    public static List<Map<String, Object>> returnLeitura(Integer maquina){
        try {
            JdbcTemplate jdbc = Connection.getConnection();
            
            List<Map<String, Object>> leituras;
            leituras = jdbc.queryForList("select top (dbo.fc_returnCountComponente(?)) id, leitura, nome_componente from vw_returnLeitura where idMaquina = ? order by id desc", maquina, maquina);
            
            //leitura = Double.valueOf(aux.get(0).get("componentes").toString());
            
            return leituras;
        } catch (DataAccessException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }
    
    public static List<Map<String, Object>> returnLeitura2(Integer maquina){
        try {
            JdbcTemplate jdbc = Connection.getConnection();
            
            String qtd = "";
            
            List<Map<String, Object>> count;
            count = jdbc.queryForList("select fc_returnCountComponente(?) as count", maquina);
            
            qtd = String.valueOf(count.get(0).get("count"));
            
             List<Map<String, Object>> leituras;
             leituras = jdbc.queryForList("select leitura, nome_componente from vw_returnLeitura where id = ? order by id desc limit "+qtd, maquina);
             
             return leituras;
        } catch (DataAccessException e) {
            System.out.println(e.getMessage());
            return null;
        }
    }
    
}
