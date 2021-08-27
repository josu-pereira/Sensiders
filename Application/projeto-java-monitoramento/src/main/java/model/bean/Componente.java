/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model.bean;

import java.util.concurrent.ThreadLocalRandom;

/**
 *
 * @author Patrick L Teixeira
 */
public class Componente {
    
    private Integer idComponente;
    private String nomeComponente;
    private String totalComponente;
    private String metricaComponente;

    public Integer getIdComponente() {
        return idComponente;
    }

    public void setIdComponente(Integer idComponente) {
        this.idComponente = idComponente;
    }

    public String getNomeComponente() {
        return nomeComponente;
    }

    public void setNomeComponente(String nomeComponente) {
        this.nomeComponente = nomeComponente;
    }

    public String getTotalComponente() {
        return totalComponente;
    }

    public void setTotalComponente(String totalComponente) {
        this.totalComponente = totalComponente;
    }

    public String getMetricaComponente() {
        return metricaComponente;
    }

    public void setMetricaComponente(String metricaComponente) {
        this.metricaComponente = metricaComponente;
    }
    
    
    
}
