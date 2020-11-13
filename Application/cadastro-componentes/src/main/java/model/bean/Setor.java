package model.bean;

public class Setor {
    
    private int idSetor;
    private String nome;
    private int fkFilial;
    private int qtdSensores;

    public int getIdSetor() {
        return idSetor;
    }

    public String getNome() {
        return nome;
    }

    public int getFkFilial() {
        return fkFilial;
    }

    public void setIdSetor(int idSetor) {
        this.idSetor = idSetor;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setFkFilial(int idFilial) {
        this.fkFilial = idFilial;
    }

    public void setQtdSensores(int qtdSensores) {
        this.qtdSensores = qtdSensores;
    }

    public int getQtdSensores() {
        return qtdSensores;
    }
    
    
    
}
