package model.bean;


public class Componente {
    private int idComponente;
    private String nomeComponente;
    private String totalComponente;
    private String metricaComponente;
    private int medidaAlertaComponente;

    public int getIdComponente() {
        return idComponente;
    }

    public void setIdComponente(int idComponente) {
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

    public int getMedidaAlertaComponente() {
        return medidaAlertaComponente;
    }

    public void setMedidaAlertaComponente(int medidaAlertaComponente) {
        this.medidaAlertaComponente = medidaAlertaComponente;
    }
}
