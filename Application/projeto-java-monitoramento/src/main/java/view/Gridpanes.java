/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package view;

/**
 *
 * @author Patrick L Teixeira
 */
public class Gridpanes {
    private String nome;
    private Double leitura;
    private String alerta;
    private Double soma = 0.0;
    private Double media;
    private String cor;
    //private Double porcentagem;
    
    public Gridpanes(){
        media = leitura;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public Double getLeitura() {
        return leitura;
    }

    public void setLeitura(Double leitura) {
        this.leitura = leitura;
    }

    public String getAlerta() {
        return alerta;
    }

    public Double getSoma() {
        return soma;
    }

    public void setSoma(Double soma) {
        this.soma = soma;
    }

    public Double getMedia() {
        return media;
    }

    public String getCor() {
        return cor;
    }
    
    public void calcMedia(Integer div){
        this.media = soma/div;
    }
    
//    public Double getPorcentagem(){
//        return porcentagem;
//    }
    
    public void medirAlerta(){
        //this.porcentagem = (leitura*100)/total;
        
        if(this.leitura <= 30){
            alerta = "baixo uso";
            cor = "-fx-text-fill: #008000";
        }else if(this.leitura<70){
            alerta= "medio uso";
            cor = "-fx-text-fill: #FFA500";
        }else{
            alerta = "alto uso";
            cor = "-fx-text-fill: #f00";
        }
    }
}
