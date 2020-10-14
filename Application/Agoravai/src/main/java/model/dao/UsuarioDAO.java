/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import javax.swing.JPanel;
import model.bean.Usuario;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author Patrick L Teixeira
 */
public class UsuarioDAO {
    
    public List<Usuario> login(String email, String senha){
        Connection conn = new Connection();
        JdbcTemplate jdbcTemplate = conn.getConnection();
        Usuario user = new Usuario();
        
        List<Usuario> lista = jdbcTemplate.query("SELECT * FROM usuario WHERE emailUsuario = ? AND senhaUsuario = ?"
                , new BeanPropertyRowMapper(Usuario.class), email, senha);
        
        return lista;
        
    }
}
