/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package view;

import java.awt.Color;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.ThreadLocalRandom;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JLabel;
import javax.swing.JProgressBar;
import model.bean.Usuario;
import model.bean.Componente;

/**
 *
 * @author haley
 */
public class TelaDashboard extends javax.swing.JFrame {
    //Integer nmr = 0;
    /**
     * Creates new form TelaDashboard
     */
    
    Componente cpu = new Componente();
    Componente ram = new Componente();
    Componente disk = new Componente();
    Componente temp = new Componente();
    
    Componente task = new Componente();
    Componente swap = new Componente();
    Componente dwnld = new Componente();
    Componente upld = new Componente();
    
    Integer cont = 0;
    
    Integer acumCpu = 0, acumRam = 0, acumDisk = 0, acumTemp = 0;
    Double mediaCpu, mediaRam, mediaDisk, mediaTemp;
    
    void gerarDados(){
        
        Timer timer = new Timer();
        timer.schedule(new TimerTask(){
            @Override
            public void run(){
                cont++;
                
                cpu.setVlr(ThreadLocalRandom.current().nextInt(0, 100));
                msg(cpu.getVlr(), "CPU", lblCpuAlerta2);
                acumCpu += cpu.getVlr();
                mediaCpu = Double.valueOf(acumCpu / cont);
                
                ram.setVlr(ThreadLocalRandom.current().nextInt(0, 100));
                msg(ram.getVlr(), "Memoria", lblMemoriaAlerta);
                acumRam += ram.getVlr();
                mediaRam = Double.valueOf(acumRam / cont);
                
                disk.setVlr(ThreadLocalRandom.current().nextInt(0, 100));
                msg(disk.getVlr(), "Disco", lblDiscoAlerta);
                acumDisk += disk.getVlr();
                mediaDisk = Double.valueOf(acumDisk / cont);            
               
                temp.setVlr(ThreadLocalRandom.current().nextInt(0, 100));
                msg(temp.getVlr(), "Temperatura", lblTempAlerta1);
                acumTemp += temp.getVlr();
                mediaTemp = Double.valueOf(acumTemp / cont);
                
                task.setVlr(ThreadLocalRandom.current().nextInt(0, 500));
                lblTrfAbertaCpu2.setText(task.getVlr().toString());
                
                dwnld.setVlr(ThreadLocalRandom.current().nextInt(0, 6000));
                lblDownload.setText(dwnld.getVlr().toString() + " KiB/s");
                
                upld.setVlr(ThreadLocalRandom.current().nextInt(0, 3000));
                lblUpload.setText(upld.getVlr().toString() + " KiB/s");
                
                swap.setVlr(ThreadLocalRandom.current().nextInt(0, 100));
                lblSwapMemoria.setText(swap.getVlr().toString() + " %");
                
                atualizarTela(lblLeituraAtualCpu2, lblMediaCpu2, cpu.getVlr(), pbCpu, mediaCpu, " %");
                atualizarTela(lblLeituraAtualMemoria, lblMediaMemoria, ram.getVlr(), pbMem, mediaRam, " %");
                atualizarTela(lblLeituraAtualTemp1, lblMediaTemp1, temp.getVlr(), pbTemp, mediaTemp, " ºC");
                atualizarTela(lblLeituraAtualDisco, lblMediaDisco, disk.getVlr(), pbDisk, mediaDisk, " %");
                
            }
        }, 1000, 3000);
        
        
    }
    
    
    
    
    void atualizarTela(JLabel labelAtual, JLabel labelMedia, Integer num, JProgressBar bar, Double media, String metrica){
        
        bar.setValue(num);
        String corMedia = cor(media);
        String corAtual = cor(Double.valueOf(num));
        labelAtual.setText(num.toString() + metrica);
        labelAtual.setForeground(Color.decode(corAtual));
        labelMedia.setText(media.toString() + metrica);
        labelMedia.setForeground(Color.decode(corMedia));
    }
    
    public String cor(Double num){
        if(num <= 30){
            return "#33FF00";
        }else if(num <= 60){
            return "#FED500";
        }else{
            return "#FF0000";
        }
    }
    
    void msg(Integer num, String txt, JLabel label){
        if(num <= 30){
            label.setForeground(Color.decode("#33FF00"));
            label.setText(txt + " em baixo uso");
        }else if(num <= 60){
            label.setForeground(Color.decode("#FED500"));
            label.setText(txt + " em médio uso");
        }else{
            label.setForeground(Color.decode("#FF0000"));
            label.setText(txt + " em alto uso");
        }
    }
    
//    void teste() throws InterruptedException{
//        while (true) {          
//            nmr++;
//            lblTempCpu1.setText(nmr.toString());
//            Thread.sleep(1000);
//        }
//    }
    
    public TelaDashboard(Usuario userLogado){
        initComponents();
        lbNomeUser.setText(userLogado.getNomeUsuario());
        gerarDados();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jPanel8 = new javax.swing.JPanel();
        jPanel3 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        btnLogout = new javax.swing.JButton();
        jLabel18 = new javax.swing.JLabel();
        lbNomeUser = new javax.swing.JLabel();
        jPanel2 = new javax.swing.JPanel();
        jPanel4 = new javax.swing.JPanel();
        jPanel9 = new javax.swing.JPanel();
        lblDiscoQntd = new javax.swing.JLabel();
        lblDiscoAlerta = new javax.swing.JLabel();
        pbDisk = new javax.swing.JProgressBar();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        lblMediaDisco = new javax.swing.JLabel();
        lblLeituraAtualDisco = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jPanel7 = new javax.swing.JPanel();
        lblMemoriaNome = new javax.swing.JLabel();
        pbMem = new javax.swing.JProgressBar();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        lblMediaMemoria = new javax.swing.JLabel();
        lblLeituraAtualMemoria = new javax.swing.JLabel();
        lblSwapMemoria = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        lblMemoriaAlerta = new javax.swing.JLabel();
        jPanel10 = new javax.swing.JPanel();
        jLabel10 = new javax.swing.JLabel();
        lblCpuNome2 = new javax.swing.JLabel();
        lblCpuAlerta2 = new javax.swing.JLabel();
        pbCpu = new javax.swing.JProgressBar();
        jLabel11 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        lblMediaCpu2 = new javax.swing.JLabel();
        lblLeituraAtualCpu2 = new javax.swing.JLabel();
        lblTrfAbertaCpu2 = new javax.swing.JLabel();
        jPanel11 = new javax.swing.JPanel();
        lblTempCpu1 = new javax.swing.JLabel();
        lblTempAlerta1 = new javax.swing.JLabel();
        pbTemp = new javax.swing.JProgressBar();
        jLabel9 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();
        lblMediaTemp1 = new javax.swing.JLabel();
        lblLeituraAtualTemp1 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel16 = new javax.swing.JLabel();
        lblDownload = new javax.swing.JLabel();
        jLabel19 = new javax.swing.JLabel();
        lblUpload = new javax.swing.JLabel();

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 141, Short.MAX_VALUE)
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 100, Short.MAX_VALUE)
        );

        jPanel8.setBackground(new java.awt.Color(255, 255, 255));
        jPanel8.setBorder(javax.swing.BorderFactory.createCompoundBorder(new javax.swing.border.LineBorder(new java.awt.Color(187, 187, 187), 1, true), new javax.swing.border.LineBorder(new java.awt.Color(255, 255, 255), 8, true)));

        javax.swing.GroupLayout jPanel8Layout = new javax.swing.GroupLayout(jPanel8);
        jPanel8.setLayout(jPanel8Layout);
        jPanel8Layout.setHorizontalGroup(
            jPanel8Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 317, Short.MAX_VALUE)
        );
        jPanel8Layout.setVerticalGroup(
            jPanel8Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 169, Short.MAX_VALUE)
        );

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(255, 255, 255));
        setMinimumSize(new java.awt.Dimension(900, 550));
        setResizable(false);

        jPanel3.setBackground(new java.awt.Color(255, 125, 125));

        jLabel1.setFont(new java.awt.Font("Montserrat", 1, 18)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(255, 255, 255));
        jLabel1.setText("Dashboard do Hardware");

        btnLogout.setBackground(new java.awt.Color(255, 125, 125));
        btnLogout.setFont(new java.awt.Font("Montserrat", 1, 18)); // NOI18N
        btnLogout.setForeground(new java.awt.Color(255, 255, 255));
        btnLogout.setText("Sair");
        btnLogout.setBorder(null);
        btnLogout.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnLogoutActionPerformed(evt);
            }
        });

        jLabel18.setFont(new java.awt.Font("Montserrat", 1, 18)); // NOI18N
        jLabel18.setForeground(new java.awt.Color(255, 255, 255));
        jLabel18.setText("Olá, ");

        lbNomeUser.setFont(new java.awt.Font("Montserrat", 1, 18)); // NOI18N
        lbNomeUser.setForeground(new java.awt.Color(255, 255, 255));
        lbNomeUser.setText("---");

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addGap(101, 101, 101)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel18)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(lbNomeUser)
                .addGap(116, 116, 116)
                .addComponent(btnLogout)
                .addGap(102, 102, 102))
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addGap(27, 27, 27)
                .addGroup(jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(btnLogout)
                    .addComponent(jLabel18)
                    .addComponent(lbNomeUser))
                .addContainerGap(56, Short.MAX_VALUE))
        );

        jPanel2.setBackground(new java.awt.Color(255, 255, 255));

        jPanel4.setBackground(new java.awt.Color(255, 255, 255));

        jPanel9.setBackground(new java.awt.Color(255, 255, 255));
        jPanel9.setBorder(javax.swing.BorderFactory.createCompoundBorder(new javax.swing.border.LineBorder(new java.awt.Color(187, 187, 187), 1, true), new javax.swing.border.LineBorder(new java.awt.Color(255, 255, 255), 8, true)));

        lblDiscoQntd.setText("1TB");

        lblDiscoAlerta.setForeground(new java.awt.Color(204, 204, 0));
        lblDiscoAlerta.setText("Disco em media de uso");

        pbDisk.setToolTipText("");
        pbDisk.setPreferredSize(new java.awt.Dimension(146, 18));

        jLabel7.setText("Média de uso:");

        jLabel8.setText("Leitura atual:");

        lblMediaDisco.setForeground(new java.awt.Color(204, 204, 0));
        lblMediaDisco.setText("55%");

        lblLeituraAtualDisco.setForeground(new java.awt.Color(204, 204, 0));
        lblLeituraAtualDisco.setText("55%");

        jLabel6.setFont(new java.awt.Font("Montserrat", 1, 22)); // NOI18N
        jLabel6.setText("Disco");

        javax.swing.GroupLayout jPanel9Layout = new javax.swing.GroupLayout(jPanel9);
        jPanel9.setLayout(jPanel9Layout);
        jPanel9Layout.setHorizontalGroup(
            jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel9Layout.createSequentialGroup()
                .addGroup(jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel9Layout.createSequentialGroup()
                        .addComponent(jLabel6)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(lblDiscoQntd)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 142, Short.MAX_VALUE)
                        .addComponent(lblDiscoAlerta))
                    .addGroup(jPanel9Layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel9Layout.createSequentialGroup()
                                .addComponent(jLabel8)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblLeituraAtualDisco))
                            .addGroup(jPanel9Layout.createSequentialGroup()
                                .addComponent(jLabel7)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblMediaDisco))
                            .addComponent(pbDisk, javax.swing.GroupLayout.PREFERRED_SIZE, 352, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        jPanel9Layout.setVerticalGroup(
            jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel9Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(lblDiscoQntd)
                    .addComponent(lblDiscoAlerta))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel7)
                    .addComponent(lblMediaDisco))
                .addGap(18, 18, 18)
                .addGroup(jPanel9Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel8)
                    .addComponent(lblLeituraAtualDisco))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(pbDisk, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(23, 23, 23))
        );

        jPanel7.setBackground(new java.awt.Color(255, 255, 255));
        jPanel7.setBorder(javax.swing.BorderFactory.createCompoundBorder(new javax.swing.border.LineBorder(new java.awt.Color(187, 187, 187), 1, true), new javax.swing.border.LineBorder(new java.awt.Color(255, 255, 255), 8, true)));

        lblMemoriaNome.setText("4GB Ram");

        pbMem.setToolTipText("");
        pbMem.setPreferredSize(new java.awt.Dimension(146, 18));

        jLabel3.setText("Média de uso:");

        jLabel4.setText("Leitura atual:");

        jLabel5.setText("Swap:");

        lblMediaMemoria.setForeground(new java.awt.Color(102, 255, 0));
        lblMediaMemoria.setText("35%");

        lblLeituraAtualMemoria.setForeground(new java.awt.Color(102, 255, 0));
        lblLeituraAtualMemoria.setText("25%");

        lblSwapMemoria.setForeground(new java.awt.Color(102, 255, 0));
        lblSwapMemoria.setText("12%");

        jLabel2.setFont(new java.awt.Font("Montserrat", 1, 24)); // NOI18N
        jLabel2.setText("Memória");

        lblMemoriaAlerta.setForeground(new java.awt.Color(51, 255, 0));
        lblMemoriaAlerta.setText("Memória em baixo uso");

        javax.swing.GroupLayout jPanel7Layout = new javax.swing.GroupLayout(jPanel7);
        jPanel7.setLayout(jPanel7Layout);
        jPanel7Layout.setHorizontalGroup(
            jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel7Layout.createSequentialGroup()
                .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel7Layout.createSequentialGroup()
                        .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(pbMem, javax.swing.GroupLayout.PREFERRED_SIZE, 352, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(jPanel7Layout.createSequentialGroup()
                                .addContainerGap()
                                .addComponent(jLabel5)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblSwapMemoria)))
                        .addGap(0, 14, Short.MAX_VALUE))
                    .addGroup(jPanel7Layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel7Layout.createSequentialGroup()
                                .addComponent(jLabel2)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(lblMemoriaNome))
                            .addGroup(jPanel7Layout.createSequentialGroup()
                                .addComponent(jLabel4)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblLeituraAtualMemoria))
                            .addGroup(jPanel7Layout.createSequentialGroup()
                                .addComponent(jLabel3)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblMediaMemoria)))
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(lblMemoriaAlerta)))
                .addContainerGap())
        );
        jPanel7Layout.setVerticalGroup(
            jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel7Layout.createSequentialGroup()
                .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(lblMemoriaNome)
                    .addComponent(lblMemoriaAlerta, javax.swing.GroupLayout.PREFERRED_SIZE, 24, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3)
                    .addComponent(lblMediaMemoria))
                .addGap(18, 18, 18)
                .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(lblLeituraAtualMemoria))
                .addGap(18, 18, 18)
                .addGroup(jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(lblSwapMemoria))
                .addGap(18, 18, 18)
                .addComponent(pbMem, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        jPanel10.setBackground(new java.awt.Color(255, 255, 255));
        jPanel10.setBorder(javax.swing.BorderFactory.createCompoundBorder(new javax.swing.border.LineBorder(new java.awt.Color(187, 187, 187), 1, true), new javax.swing.border.LineBorder(new java.awt.Color(255, 255, 255), 8, true)));

        jLabel10.setFont(new java.awt.Font("Montserrat", 1, 24)); // NOI18N
        jLabel10.setText("CPU");

        lblCpuNome2.setText("I3 3333 2.3GHz");

        lblCpuAlerta2.setForeground(new java.awt.Color(255, 0, 51));
        lblCpuAlerta2.setText("CPU em uso alto");

        pbCpu.setToolTipText("");
        pbCpu.setPreferredSize(new java.awt.Dimension(146, 18));

        jLabel11.setText("Média de uso:");

        jLabel12.setText("Leitura atual:");

        jLabel13.setText("Qntd de tarefas abertas:");

        lblMediaCpu2.setForeground(new java.awt.Color(204, 204, 0));
        lblMediaCpu2.setText("55%");

        lblLeituraAtualCpu2.setForeground(new java.awt.Color(255, 0, 0));
        lblLeituraAtualCpu2.setText("80%");

        lblTrfAbertaCpu2.setForeground(new java.awt.Color(204, 204, 0));
        lblTrfAbertaCpu2.setText("4");

        javax.swing.GroupLayout jPanel10Layout = new javax.swing.GroupLayout(jPanel10);
        jPanel10.setLayout(jPanel10Layout);
        jPanel10Layout.setHorizontalGroup(
            jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel10Layout.createSequentialGroup()
                .addGroup(jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel10Layout.createSequentialGroup()
                        .addComponent(jLabel13)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lblTrfAbertaCpu2))
                    .addComponent(pbCpu, javax.swing.GroupLayout.PREFERRED_SIZE, 340, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(jPanel10Layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel10Layout.createSequentialGroup()
                                .addComponent(jLabel10)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblCpuNome2)
                                .addGap(69, 69, 69)
                                .addComponent(lblCpuAlerta2))
                            .addGroup(jPanel10Layout.createSequentialGroup()
                                .addComponent(jLabel11)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblMediaCpu2))
                            .addGroup(jPanel10Layout.createSequentialGroup()
                                .addComponent(jLabel12)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblLeituraAtualCpu2)))))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel10Layout.setVerticalGroup(
            jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel10Layout.createSequentialGroup()
                .addGroup(jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel10)
                    .addComponent(lblCpuNome2)
                    .addComponent(lblCpuAlerta2))
                .addGap(18, 18, 18)
                .addGroup(jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel11)
                    .addComponent(lblMediaCpu2))
                .addGap(18, 18, 18)
                .addGroup(jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel12)
                    .addComponent(lblLeituraAtualCpu2))
                .addGap(18, 18, 18)
                .addGroup(jPanel10Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel13)
                    .addComponent(lblTrfAbertaCpu2))
                .addGap(18, 18, 18)
                .addComponent(pbCpu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(39, Short.MAX_VALUE))
        );

        jPanel11.setBackground(new java.awt.Color(255, 255, 255));
        jPanel11.setBorder(javax.swing.BorderFactory.createCompoundBorder(new javax.swing.border.LineBorder(new java.awt.Color(187, 187, 187), 1, true), new javax.swing.border.LineBorder(new java.awt.Color(255, 255, 255), 8, true)));

        lblTempCpu1.setText("100C°");

        lblTempAlerta1.setForeground(new java.awt.Color(102, 255, 0));
        lblTempAlerta1.setText("Temperatura estavel");

        pbTemp.setToolTipText("");
        pbTemp.setPreferredSize(new java.awt.Dimension(146, 18));

        jLabel9.setText("Média de uso:");

        jLabel14.setText("Leitura atual:");

        lblMediaTemp1.setForeground(new java.awt.Color(102, 255, 0));
        lblMediaTemp1.setText("25%");

        lblLeituraAtualTemp1.setForeground(new java.awt.Color(102, 255, 0));
        lblLeituraAtualTemp1.setText("45%");

        jLabel15.setFont(new java.awt.Font("Montserrat", 1, 22)); // NOI18N
        jLabel15.setText("Temperatura");

        javax.swing.GroupLayout jPanel11Layout = new javax.swing.GroupLayout(jPanel11);
        jPanel11.setLayout(jPanel11Layout);
        jPanel11Layout.setHorizontalGroup(
            jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel11Layout.createSequentialGroup()
                .addComponent(jLabel15)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(lblTempCpu1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(lblTempAlerta1))
            .addGroup(jPanel11Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel11Layout.createSequentialGroup()
                        .addGroup(jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel11Layout.createSequentialGroup()
                                .addComponent(jLabel14)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblLeituraAtualTemp1))
                            .addGroup(jPanel11Layout.createSequentialGroup()
                                .addComponent(jLabel9)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lblMediaTemp1)))
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel11Layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(pbTemp, javax.swing.GroupLayout.PREFERRED_SIZE, 352, javax.swing.GroupLayout.PREFERRED_SIZE))))
        );
        jPanel11Layout.setVerticalGroup(
            jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel11Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel15)
                    .addComponent(lblTempCpu1)
                    .addComponent(lblTempAlerta1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 40, Short.MAX_VALUE)
                .addGroup(jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel9)
                    .addComponent(lblMediaTemp1))
                .addGap(18, 18, 18)
                .addGroup(jPanel11Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel14)
                    .addComponent(lblLeituraAtualTemp1))
                .addGap(18, 18, 18)
                .addComponent(pbTemp, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(23, 23, 23))
        );

        jLabel16.setText("Velocidade Download:");

        lblDownload.setText("334 KiB/s");

        jLabel19.setText("Velocidade Upload:");

        lblUpload.setText("334 KiB/s");

        javax.swing.GroupLayout jPanel4Layout = new javax.swing.GroupLayout(jPanel4);
        jPanel4.setLayout(jPanel4Layout);
        jPanel4Layout.setHorizontalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel4Layout.createSequentialGroup()
                .addGap(66, 66, 66)
                .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel4Layout.createSequentialGroup()
                        .addComponent(jLabel16)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lblDownload)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel19)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lblUpload))
                    .addGroup(jPanel4Layout.createSequentialGroup()
                        .addGap(6, 6, 6)
                        .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jPanel11, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jPanel10, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jPanel7, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jPanel9, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
                .addContainerGap(32, Short.MAX_VALUE))
        );
        jPanel4Layout.setVerticalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel4Layout.createSequentialGroup()
                .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jPanel10, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jPanel7, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(jPanel9, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jPanel11, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel16)
                    .addComponent(lblDownload)
                    .addComponent(jLabel19)
                    .addComponent(lblUpload))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addComponent(jPanel2, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, 0)
                .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnLogoutActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnLogoutActionPerformed
        // TODO add your handling code here:
        setVisible(false);
        dispose();
        
        TelaLogin tl = new TelaLogin();
        tl.setVisible(true);
    }//GEN-LAST:event_btnLogoutActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(TelaDashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(TelaDashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(TelaDashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(TelaDashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>
        
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
               
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnLogout;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLabel18;
    private javax.swing.JLabel jLabel19;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel10;
    private javax.swing.JPanel jPanel11;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel7;
    private javax.swing.JPanel jPanel8;
    private javax.swing.JPanel jPanel9;
    private javax.swing.JLabel lbNomeUser;
    private javax.swing.JLabel lblCpuAlerta2;
    private javax.swing.JLabel lblCpuNome2;
    private javax.swing.JLabel lblDiscoAlerta;
    private javax.swing.JLabel lblDiscoQntd;
    private javax.swing.JLabel lblDownload;
    private javax.swing.JLabel lblLeituraAtualCpu2;
    private javax.swing.JLabel lblLeituraAtualDisco;
    private javax.swing.JLabel lblLeituraAtualMemoria;
    private javax.swing.JLabel lblLeituraAtualTemp1;
    private javax.swing.JLabel lblMediaCpu2;
    private javax.swing.JLabel lblMediaDisco;
    private javax.swing.JLabel lblMediaMemoria;
    private javax.swing.JLabel lblMediaTemp1;
    private javax.swing.JLabel lblMemoriaAlerta;
    private javax.swing.JLabel lblMemoriaNome;
    private javax.swing.JLabel lblSwapMemoria;
    private javax.swing.JLabel lblTempAlerta1;
    private javax.swing.JLabel lblTempCpu1;
    private javax.swing.JLabel lblTrfAbertaCpu2;
    private javax.swing.JLabel lblUpload;
    private javax.swing.JProgressBar pbCpu;
    private javax.swing.JProgressBar pbDisk;
    private javax.swing.JProgressBar pbMem;
    private javax.swing.JProgressBar pbTemp;
    // End of variables declaration//GEN-END:variables
}
