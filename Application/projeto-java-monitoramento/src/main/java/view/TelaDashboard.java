package view;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import model.bean.Usuario;
import styles.GlobalStyles;

public class TelaDashboard extends Application {

    private int posX = 1;
    private int posY = 1;
    private int count = 0;
    private Usuario user;
    private int idMaquina;
    private String descricaoMaquina;

    public TelaDashboard(Usuario user, int idMaquina, String descricaoMaquina) {
        this.user = user;
        this.idMaquina = idMaquina;
        this.descricaoMaquina = descricaoMaquina;
    }

    GlobalStyles globalStyles = new GlobalStyles();

    public void start(Stage stage) {

        // PANE
        Pane pane = new Pane();
        stage.setTitle("Dashboard");
        stage.setResizable(false);
        stage.setScene(new Scene(pane, 1300, 700));

        // HEADER
        Rectangle header = new Rectangle(0, 0, pane.getWidth(), 150);
        header.toFront();

        // LABELS
        Label lbNomeMaquina = new Label(descricaoMaquina);
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

//        for para ter 4 box sendo exibidas na tela
        for (int i = 0; i < 4; i++) {

            // Labels dos gridpanes
            Label lbNomeComponente = new Label("CPU");
            lbNomeComponente.setLayoutX(27);
            lbNomeComponente.setLayoutY(17);
            lbNomeComponente.setStyle(globalStyles.getStyleLabelComponente());

            Label lbComponenteDescricao = new Label("Intel i3 7200 2.30GHz");
            lbComponenteDescricao.setLayoutX(lbNomeComponente.getLayoutX() + 60);
            lbComponenteDescricao.setLayoutY(25);
            lbComponenteDescricao.setStyle(globalStyles.getStyleLabels());

            Label lbSituacaoComponente = new Label("CPU em alto uso");
            lbSituacaoComponente.setLayoutX(390);
            lbSituacaoComponente.setLayoutY(25);
            lbSituacaoComponente.setStyle(globalStyles.getStyleLabels() + "-fx-text-fill: red");

            Label lbMediaDeUso = new Label("Média de Uso: ");
            lbMediaDeUso.setLayoutX(lbNomeComponente.getLayoutX());
            lbMediaDeUso.setLayoutY(70);
            lbMediaDeUso.setStyle(globalStyles.getStyleLabelsDashboard());

            Label lbLeituraAtual = new Label("Leitura Atual: ");
            lbLeituraAtual.setLayoutX(lbMediaDeUso.getLayoutX());
            lbLeituraAtual.setLayoutY(100);
            lbLeituraAtual.setStyle(globalStyles.getStyleLabelsDashboard());

            Label lbQtdTarefasExecutadas = new Label("Qtd de Tarefas executadas: ");
            lbQtdTarefasExecutadas.setLayoutX(lbMediaDeUso.getLayoutX());
            lbQtdTarefasExecutadas.setLayoutY(130);
            lbQtdTarefasExecutadas.setStyle(globalStyles.getStyleLabelsDashboard());

            Label lbValorMediaDeUso = new Label("55%");
            lbValorMediaDeUso.setLayoutX(lbMediaDeUso.getLayoutX() + 120);
            lbValorMediaDeUso.setLayoutY(lbMediaDeUso.getLayoutY());
            lbValorMediaDeUso.setStyle(globalStyles.getStyleLabelsDashboard());

            Label lbValorLeituraAtual = new Label("80%");
            lbValorLeituraAtual.setLayoutX(lbLeituraAtual.getLayoutX() + 120);
            lbValorLeituraAtual.setLayoutY(lbLeituraAtual.getLayoutY());
            lbValorLeituraAtual.setStyle(globalStyles.getStyleLabelsDashboard());

            Label lbValorQtdTarefasExecutadas = new Label("4");
            lbValorQtdTarefasExecutadas.setLayoutX(lbQtdTarefasExecutadas.getLayoutX() + 230);
            lbValorQtdTarefasExecutadas.setLayoutY(lbQtdTarefasExecutadas.getLayoutY());
            lbValorQtdTarefasExecutadas.setStyle(globalStyles.getStyleLabelsDashboard());

            // barra de progresso
            ProgressBar pb = new ProgressBar(0.8);
            pb.setLayoutX(lbNomeComponente.getLayoutX());
            pb.setLayoutY(200);
            pb.setPrefWidth(470);
            pb.prefHeight(30);
            pb.setStyle(globalStyles.getSyleProgressBar());

            Rectangle boxMaquina = new Rectangle(posX, 200, 518, 260);
            boxMaquina.setStyle("-fx-fill: #FFF;");
            boxMaquina.setCursor(Cursor.HAND);
            boxMaquina.setArcHeight(8);
            boxMaquina.setArcWidth(8);

            Pane paneComponente = new Pane();
            paneComponente.setPrefWidth(boxMaquina.getWidth());
            paneComponente.setPrefHeight(boxMaquina.getHeight());

            // Para quando clicar na "boxMaquina"
            boxMaquina.setOnMouseClicked(new EventHandler<MouseEvent>() {
                @Override
                public void handle(MouseEvent t) {

                }
            });

            // if pra ter duas colunas
            if (count == 2) {
                posX++;
                posY = 1;
                count = 0;
            }
            count++;
            posY++;

            gridPane.add(boxMaquina, posY, posX);
            gridPane.add(paneComponente, posY, posX);
            //getChildren das informações do componente
            paneComponente.getChildren().add(lbNomeComponente);
            paneComponente.getChildren().add(lbComponenteDescricao);
            paneComponente.getChildren().add(lbSituacaoComponente);

            //getChildren dos dados do componente
            paneComponente.getChildren().add(lbMediaDeUso);
            paneComponente.getChildren().add(lbLeituraAtual);
            paneComponente.getChildren().add(lbQtdTarefasExecutadas);
            paneComponente.getChildren().add(lbValorMediaDeUso);
            paneComponente.getChildren().add(lbValorLeituraAtual);
            paneComponente.getChildren().add(lbValorQtdTarefasExecutadas);
            paneComponente.getChildren().add(pb);

        } //Fim do for

        // Dados sorbe velocidade de download e upload
        Label lbVelocDown = new Label("Veloc. Down: ");
        lbVelocDown.setLayoutX(120);
        lbVelocDown.setLayoutY(675);
        lbVelocDown.setStyle(globalStyles.getStyleLabels());

        Label lbValorVelocDown = new Label("859KiB/s");
        lbValorVelocDown.setLayoutX(lbVelocDown.getLayoutX() + 95);
        lbValorVelocDown.setLayoutY(675);
        lbValorVelocDown.setStyle(globalStyles.getStyleLabels());

        Label lbVelocUp = new Label("Veloc. Up: ");
        lbVelocUp.setLayoutX(lbValorVelocDown.getLayoutX() + 90);
        lbVelocUp.setLayoutY(675);
        lbVelocUp.setStyle(globalStyles.getStyleLabels());

        Label lbValorVelocUp = new Label("265KiB/s");
        lbValorVelocUp.setLayoutX(lbVelocUp.getLayoutX() + 70);
        lbValorVelocUp.setLayoutY(675);
        lbValorVelocUp.setStyle(globalStyles.getStyleLabels());

        // Adicionando estilos
        pane.setStyle(globalStyles.getBackgroundPage());
        header.setStyle(globalStyles.getStyleHeader());
        lbNomeMaquina.setStyle(globalStyles.getStyleTitle());
        lbVoltar.setStyle(globalStyles.getStyleTitle());

        // Ações
        lbVoltar.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent t) {
                new TelaListaMaquinas(user).start(stage);
            }
        });

        // Adicionando à tela
        pane.getChildren().add(header);
        pane.getChildren().add(lbNomeMaquina);
        pane.getChildren().add(lbVoltar);
        pane.getChildren().add(gridPane);

        //getChildren veloc down e up
        pane.getChildren().add(lbVelocDown);
        pane.getChildren().add(lbValorVelocDown);
        pane.getChildren().add(lbVelocUp);
        pane.getChildren().add(lbValorVelocUp);

        stage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
