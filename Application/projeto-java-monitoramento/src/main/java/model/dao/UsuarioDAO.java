/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.dao;

import connection.Connection;
import java.util.List;
import model.bean.Usuario;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author Patrick L Teixeira
 */
public class UsuarioDAO {
    
    public static Usuario login(String email, String senha){
        
        try {
            JdbcTemplate jdbcTemplate = Connection.getConnection();
            Usuario user = new Usuario();

            List<Usuario> lista = jdbcTemplate.query("SELECT * FROM usuario WHERE emailUsuario = ? AND senhaUsuario = ?"
                    , new BeanPropertyRowMapper(Usuario.class), email, senha);
            
            if(lista.isEmpty()){
                return null;
            }else{
                 lista.forEach(u -> {
                    user.setIdUsuario(u.getIdUsuario());
                    user.setEmailUsuario(u.getEmailUsuario());
                    user.setSenhaUsuario(u.getSenhaUsuario());
                    user.setNomeUsuario(u.getNomeUsuario());
                    user.setFkIdFilial(u.getFkIdFilial());
                 });
                 return user;
            }
        } catch (DataAccessException e) {
            System.out.println(e.getMessage());
            return null;
        }
        
    }
}
