package com.haley.dashboard;

public class Users {

    private Integer id;
    private String emailUsuario;
    private String senhaUsuario;
    private String nomeUsuario;
    private Integer fkIdFilial;

    public Integer getId() {
        return id;
    }

    public String getEmailUsuario() {
        return emailUsuario;
    }

    public String getSenhaUsuario() {
        return senhaUsuario;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public Integer getFkIdFilial() {
        return fkIdFilial;
    }
    
}
