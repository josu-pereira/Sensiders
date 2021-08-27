package model.bean;

public class Maquina {
    
    private int idMaquina;
    private String descricaoMaquina;
    private int fkFilial;
    private String hashmac;

    public int getIdMaquina() {
        return idMaquina;
    }

    public void setIdMaquina(int idMaquina) {
        this.idMaquina = idMaquina;
    }

    public String getDescricaoMaquina() {
        return descricaoMaquina;
    }

    public void setDescricaoMaquina(String descricaoMaquina) {
        this.descricaoMaquina = descricaoMaquina;
    }

    public int getFkFilial() {
        return fkFilial;
    }

    public void setFkFilial(int fkFilial) {
        this.fkFilial = fkFilial;
    }

    public String getHashmac() {
        return hashmac;
    }

    public void setHashmac(String hashmac) {
        this.hashmac = hashmac;
    }
    
    

}
