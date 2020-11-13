
package view;

import component.styles.GlobalStyles;
import java.util.*;
import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.geometry.HPos;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import model.bean.Maquina;
import model.dao.MaquinaDAO;

public class TelaListaMaquinas extends Application {
    
    private int posX = 1;
    private int posY = 1;
    private int count = 0;
    
    private int idFilial;

    public TelaListaMaquinas(int idFilial) {
        this.idFilial = idFilial;
    }
    
    GlobalStyles globalStyles = new GlobalStyles();
    
    public void start(Stage stage) {
        
        System.out.println(idFilial);
        // Layout
        Pane pane = new Pane();  
        GridPane gridPane = new GridPane();
    
      
        gridPane.setLayoutX(80);
        gridPane.setLayoutY(100);
        gridPane.setHgap(20);
        gridPane.setVgap(20);
        
        stage.setTitle("Setores");
        stage.setResizable(false);
        stage.setScene(new Scene(pane, 1300, 700));
        
        // HEADER
        Rectangle header = new Rectangle(0, 0, pane.getWidth(), 150);
        header.toBack();
        
        // Labels
        Label lbTitlPage = new Label("Selecionar máquina");
        lbTitlPage.setLayoutX(120);
        lbTitlPage.setLayoutY(65);
        
        Label lbSair = new Label("Sair");
        lbSair.setLayoutX(1140);
        lbSair.setLayoutY(65);
        lbSair.setCursor(Cursor.HAND);
        
       /*
        Rectangle boxSetor = new Rectangle(120, 200, 250, 150);
        boxSetor.setStyle("-fx-fill: #FFF;");
        boxSetor.setArcHeight(8);
        boxSetor.setArcWidth(8);*/
        
        
        
        
        //TextField
        TextField tfPesquisar = new TextField();
        tfPesquisar.setLayoutX(120);
        tfPesquisar.setLayoutY(130);
        tfPesquisar.setPrefWidth(1060);
        tfPesquisar.setPrefHeight(50);
       
        
        // Adicionando os styles
        pane.setStyle(globalStyles.getBackgroundPage());
        header.setStyle(globalStyles.getStyleHeader());
        lbTitlPage.setStyle(globalStyles.getStyleTitle());
        tfPesquisar.setStyle(globalStyles.getStyleTfSearch());
        lbSair.setStyle(globalStyles.getStyleTitle());

        List<Maquina> listaSetores = new MaquinaDAO().selectComponente(idFilial);
        
        posX = 1;
        posY = 1;
        count = 0;

        listaSetores.forEach(s -> {
            Label lbDescricaoMaquina = new Label(s.getDescricaoMaquina());
            lbDescricaoMaquina.setLayoutX(250);
            lbDescricaoMaquina.setStyle(globalStyles.getStyleLabels());
            
            Rectangle boxMaquina = new Rectangle(posX, 200, 250, 150);
            boxMaquina.setStyle("-fx-fill: #FFF;");
            boxMaquina.setCursor(Cursor.HAND);
            boxMaquina.setArcHeight(8);
            boxMaquina.setArcWidth(8);
            
            if(count == 4) {
               posX++;
               posY = 1;
               count = 0;
            }
            
            count++;
            posY++;
            gridPane.setHalignment(lbDescricaoMaquina, HPos.CENTER);
            gridPane.add(boxMaquina, posY, posX);
            gridPane.add(lbDescricaoMaquina, posY, posX);
        
        });
        
        
        // Adicionando ao layout
        pane.getChildren().add(header);
        pane.getChildren().add(gridPane);
        //boxSetor.toFront();
        //pane.getChildren().add(group);
        
        pane.getChildren().add(lbTitlPage);
        //pane.getChildren().add(tfPesquisar);
        pane.getChildren().add(lbSair);
        
        // Ações
        
        // Sair
        lbSair.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent t) {
                
                new TelaLogin().start(stage);
            }
            
        });
        
        
        
        
        stage.show();
        
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
