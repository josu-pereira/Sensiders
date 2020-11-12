/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.bean;

import java.util.*;

/**
 *
 * @author Patrick L Teixeira
 */
public class Maquina {
    
    private Integer idMaquina;
    private String descricaoMaquina; 
    private Integer fkFilial;
    private String hashmac;
    private final List<Componente> componentes = null;

    public Integer getIdMaquina() {
        return idMaquina;
    }

    public void setIdMaquina(Integer idMaquina) {
        this.idMaquina = idMaquina;
    }

    public String getDescricaoMaquina() {
        return descricaoMaquina;
    }

    public void setDescricaoMaquina(String descricaoMaquina) {
        this.descricaoMaquina = descricaoMaquina;
    }

    public Integer getFkFilial() {
        return fkFilial;
    }

    public void setFkFilial(Integer fkFilial) {
        this.fkFilial = fkFilial;
    }

    public String getHashmac() {
        return hashmac;
    }

    public void setHashmac(String hashmac) {
        this.hashmac = hashmac;
    }
    
    
    
}
