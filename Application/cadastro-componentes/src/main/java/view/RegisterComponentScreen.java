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


public class RegisterComponentScreen extends Application {
 
    GlobalStyles globalStyles = new GlobalStyles();
    
    public void start(Stage stage) {
        
     
        
        stage.setTitle("Cadastro de um componente");
        stage.setResizable(false);
        
        // Layouts
        Pane pane = new Pane();
    
        GridPane gridpane = new GridPane();
        gridpane.setLayoutX(60);
        gridpane.setLayoutY(100);
        pane.getChildren().add(gridpane);
                
        gridpane.setHgap(10);
        gridpane.setVgap(10);
        //gridpane.setAlignment(Pos.CENTER);
        
        
        // HEADER
        Rectangle header = new Rectangle(0, 0, 1000, 100);
        header.setStyle(globalStyles.getStyleHeader());
        pane.getChildren().add(header);
        
        // BOX FORM
        Rectangle boxForm = new Rectangle(50, 75, 400, 450);
        boxForm.setStyle("-fx-fill: #FFF;");
        boxForm.setArcHeight(8);
        boxForm.setArcWidth(8);
        pane.getChildren().add(boxForm);
               
        
        
        Label lbMensagemResultado = new Label();
        Label lbTitulo = new Label("Adicionar componente novo");
     
        Label lbNomeComponente = new Label("Nome");
        Label lbMetricaComponente = new Label("Métrica");
        Label lbTotalLeituraComponente = new Label("Total da leitura");
        
        TextField tfNomeComponente = new TextField();
        TextField tfMetricaComponente = new TextField();
        TextField tfTotalLeituraComponente = new TextField();
        
        Button btnCadastrarComponente = new Button("Salvar");
        btnCadastrarComponente.setCursor(Cursor.HAND);
        
        
        
        tfNomeComponente.setPrefWidth(350);
        tfNomeComponente.setPrefHeight(35);
        
        tfMetricaComponente.setPrefWidth(tfNomeComponente.getPrefWidth());
        tfMetricaComponente.setPrefHeight(tfNomeComponente.getPrefHeight());
        
        tfTotalLeituraComponente.setPrefWidth(tfNomeComponente.getPrefWidth());
        tfTotalLeituraComponente.setPrefHeight(tfNomeComponente.getPrefHeight());
        
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
        
        gridpane.add(btnCadastrarComponente, 1, 8);
        
        gridpane.add(lbMensagemResultado, 1, 9);
        
        // Adicionando os styles
        pane.setStyle(globalStyles.getBackgroundPage());
        
        lbTitulo.setStyle(globalStyles.getStyleTitle());
        tfNomeComponente.setStyle(globalStyles.getStyleTextField());
        tfMetricaComponente.setStyle(globalStyles.getStyleTextField());
        tfTotalLeituraComponente.setStyle(globalStyles.getStyleTextField());
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
                
                
                if(nomeComponente.equals("") | metricaComponente.equals("") | totalLeituraComponente.equals("")) {
                    lbMensagemResultado.setStyle(globalStyles.getStyleErrorMessage());
                    lbMensagemResultado.setText("Opps... Preencha os campos!");
                } else {
                    
                    int dialogResult = JOptionPane.showConfirmDialog(null, 
                        "Deseja mesmo criar esse componente?", "Atenção", 
                        JOptionPane.OK_CANCEL_OPTION, JOptionPane.INFORMATION_MESSAGE);
                
                
                    if(dialogResult == JOptionPane.YES_OPTION) {
                        System.out.println("FOI MANOO");
                        JOptionPane.showMessageDialog(null, "Componente criado com sucesso");
                    }
                }
                
                System.out.println(nomeComponente +" "+ metricaComponente +" "+ totalLeituraComponente);
                
            };
        });
        
        
        gridpane.toFront();
        stage.setScene(new Scene(pane, 500, 600));
        stage.show();
        
    }
      
    public static void main(String[] args) {
        launch(args);
    }
    
}
