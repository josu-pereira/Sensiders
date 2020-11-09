package view;

import component.styles.GlobalStyles;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javax.swing.JOptionPane;
import model.bean.Componente;
import model.dao.ComponenteDAO;


public class RegisterComponentScreen extends Application {
 
    GlobalStyles globalStyles = new GlobalStyles();
    
    public void start(Stage stage) {
        
        // Layouts
        Pane pane = new Pane();
        
        stage.setTitle("Cadastro de um componente");
        stage.setResizable(false);
        stage.setScene(new Scene(pane, 1300, 700));
        
        
    
        GridPane gridpane = new GridPane();
        gridpane.setLayoutX(495);
        gridpane.setLayoutY(180);
        pane.getChildren().add(gridpane);
                
        gridpane.setHgap(10);
        gridpane.setVgap(10);
        //gridpane.setAlignment(Pos.CENTER);
        
        
        // HEADER
        Rectangle header = new Rectangle(0, 0, pane.getWidth(), 200);
        
        pane.getChildren().add(header);
        
        // BOX FORM
        Rectangle boxForm = new Rectangle(480, 150, 400, 480);
        boxForm.setStyle("-fx-fill: #FFF;");
        boxForm.setArcHeight(8);
        boxForm.setArcWidth(8);
        pane.getChildren().add(boxForm);
               
        
        
        Label lbMensagemResultado = new Label();
        Label lbTitulo = new Label("Adicionar componente novo");
     
        Label lbNomeComponente = new Label("Nome");
        Label lbMetricaComponente = new Label("Métrica");
        Label lbTotalLeituraComponente = new Label("Total da leitura");
        Label lbMedidaAlertaComponente = new Label("Medida de alerta");
        
        TextField tfNomeComponente = new TextField();
        TextField tfMetricaComponente = new TextField();
        TextField tfTotalLeituraComponente = new TextField();
        TextField tfMedidaAlertaComponente = new TextField();
        
        Button btnCadastrarComponente = new Button("Salvar");
        btnCadastrarComponente.setCursor(Cursor.HAND);
        
        
        
        tfNomeComponente.setPrefWidth(350);
        tfNomeComponente.setPrefHeight(35);
        
        tfMetricaComponente.setPrefWidth(tfNomeComponente.getPrefWidth());
        tfMetricaComponente.setPrefHeight(tfNomeComponente.getPrefHeight());
        
        tfTotalLeituraComponente.setPrefWidth(tfNomeComponente.getPrefWidth());
        tfTotalLeituraComponente.setPrefHeight(tfNomeComponente.getPrefHeight());
        
        tfMedidaAlertaComponente.setPrefWidth(tfNomeComponente.getPrefWidth());
        tfMedidaAlertaComponente.setPrefHeight(tfNomeComponente.getPrefHeight());
        
        btnCadastrarComponente.setPrefWidth(350);
        btnCadastrarComponente.setPrefHeight(35);
        
        
        // Adicionando na tela
        gridpane.add(lbTitulo, 1, 1);
        gridpane.add(lbNomeComponente, 1, 2);
        gridpane.add(tfNomeComponente, 1, 3);
        
        gridpane.add(lbMetricaComponente, 1, 4);
        gridpane.add(tfMetricaComponente, 1, 5);
        
        gridpane.add(lbTotalLeituraComponente, 1, 6);
        gridpane.add(tfTotalLeituraComponente, 1, 7);
        
        gridpane.add(lbMedidaAlertaComponente, 1, 8);
        gridpane.add(tfMedidaAlertaComponente, 1, 9);
        
        gridpane.add(btnCadastrarComponente, 1, 11);
        
        gridpane.add(lbMensagemResultado, 1, 12);
        
        // Adicionando os styles
        pane.setStyle(globalStyles.getBackgroundPage());
        
        header.setStyle(globalStyles.getStyleHeader());
        
        lbTitulo.setStyle(globalStyles.getStyleTitle());
        tfNomeComponente.setStyle(globalStyles.getStyleTextField());
        tfMetricaComponente.setStyle(globalStyles.getStyleTextField());
        tfTotalLeituraComponente.setStyle(globalStyles.getStyleTextField());
        tfMedidaAlertaComponente.setStyle(globalStyles.getStyleTextField());
        
        btnCadastrarComponente.setStyle(globalStyles.getStyleButtonConfirm());

        
        /*
        *   AÇÔES PARA O BOTÃO
        */
        
        btnCadastrarComponente.setOnAction(new EventHandler<ActionEvent>() {
            
            
            @Override
            public void handle(ActionEvent t) {
                
                
                String nomeComponente =  tfNomeComponente.getText().trim();
                String metricaComponente = tfMetricaComponente.getText().trim();
                String totalLeituraComponente = tfTotalLeituraComponente.getText().trim();
                String medidaAlertaComponente = tfMedidaAlertaComponente.getText().trim();
                
                
                if(nomeComponente.equals("") | metricaComponente.equals("") | totalLeituraComponente.equals("")
                        | medidaAlertaComponente.equals(" ")
                ) {
                    lbMensagemResultado.setStyle(globalStyles.getStyleErrorMessage());
                    lbMensagemResultado.setText("Opps... Preencha os campos!");
                } else {
                    
                    int dialogResult = JOptionPane.showConfirmDialog(null, 
                        "Deseja mesmo criar esse componente?", "Atenção", 
                        JOptionPane.OK_CANCEL_OPTION, JOptionPane.INFORMATION_MESSAGE);
                
                
                    if(dialogResult == JOptionPane.YES_OPTION) {
                        
                        Componente comp = new Componente();
                        
                        comp.setNomeComponente(nomeComponente);
                        comp.setMetricaComponente(metricaComponente);
                        comp.setTotalComponente(totalLeituraComponente);
                        comp.setMedidaAlertaComponente(Integer.valueOf(medidaAlertaComponente));
                        
                        
                        ComponenteDAO componenteDAO = new ComponenteDAO();
                        componenteDAO.insertComponente(comp);
                        
                        
                        /*
                        JOptionPane.showMessageDialog(null, "Componente criado com sucesso");*/
                    }
                }
                
                System.out.println(nomeComponente +" "+ metricaComponente +" "+ totalLeituraComponente + " " + medidaAlertaComponente);
                
            };
        });
        
        
        gridpane.toFront();
       
        stage.show();
        
    }
      
    public static void main(String[] args) {
        launch(args);
    }
    
}
