package view;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.geometry.HPos;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import styles.GlobalStyles;

public class TelaDashboard extends Application {
    
    private int posX = 1;
    private int posY = 1;
    private int count = 0;
    
    GlobalStyles globalStyles = new GlobalStyles();
    
    public void start(Stage stage) {
        Pane pane = new Pane();
        stage.setTitle("Dashboard");
        stage.setResizable(false);
        stage.setScene(new Scene(pane, 1300, 700));

        // HEADER
        Rectangle header = new Rectangle(0, 0, pane.getWidth(), 150);
        header.toFront();

        // LABELS
        Label lbNomeMaquina = new Label("Máquina 1");
        lbNomeMaquina.setLayoutX(120);
        lbNomeMaquina.setLayoutY(45);
        
        Label lbVoltar = new Label("Voltar");
        lbVoltar.setLayoutX(1140);
        lbVoltar.setLayoutY(lbNomeMaquina.getLayoutY());
        lbVoltar.setCursor(Cursor.HAND);

        // Box componentes
        GridPane gridPane = new GridPane();
        gridPane.toFront();
        
        gridPane.setLayoutX(50);
        gridPane.setLayoutY(75);
        gridPane.setHgap(35);
        gridPane.setVgap(35);
        
        posX = 1;
        posY = 1;
        count = 0;

//        listaSetores.forEach(s -> {
        for (int i = 0; i < 4; i++) {
            BorderPane paneComponente = new BorderPane();
//            paneComponente.setPrefWidth(300);
//            paneComponente.setPrefHeight(300);
            Label lbNomeComponente = new Label("NOME COMP.");
            lbNomeComponente.setLayoutX(0);
            lbNomeComponente.setLayoutY(0);
            lbNomeComponente.setStyle(globalStyles.getStyleLabels());
            
            Rectangle boxMaquina = new Rectangle(posX, 200, 518, 260);
            boxMaquina.setStyle("-fx-fill: #FFF;");
            boxMaquina.setCursor(Cursor.HAND);
            boxMaquina.setArcHeight(8);
            boxMaquina.setArcWidth(8);

            // Para quando clicar na "boxMaquina"
            boxMaquina.setOnMouseClicked(new EventHandler<MouseEvent>() {
                @Override
                public void handle(MouseEvent t) {
//                    System.out.println(s.getDescricaoMaquina());
                }
            });
            
            if (count == 2) {
                posX++;
                posY = 1;
                count = 0;
            }
            
            count++;
            posY++;
//            gridPane.setHalignment(lbNomeComponente, HPos.CENTER);
//            paneComponente.getChildren().add(lbNomeComponente);  
            paneComponente.setRight(lbNomeComponente);
            gridPane.add(boxMaquina, posY, posX);
            gridPane.add(paneComponente, posY, posX);
            gridPane.add(lbNomeComponente, posY, posX);
        }

//        });
        // Adicionando estilos
        pane.setStyle(globalStyles.getBackgroundPage());
        header.setStyle(globalStyles.getStyleHeader());
        lbNomeMaquina.setStyle(globalStyles.getStyleTitle());
        lbVoltar.setStyle(globalStyles.getStyleTitle());

        // Adicionando à tela
        pane.getChildren().add(header);
        pane.getChildren().add(lbNomeMaquina);
        pane.getChildren().add(lbVoltar);
        pane.getChildren().add(gridPane);
        
        stage.show();
        
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
