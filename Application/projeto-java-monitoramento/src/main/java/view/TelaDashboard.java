package view;

/**
 *
 * @author josu
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.ScrollPane;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import model.bean.Componente;
import model.bean.Usuario;
import model.dao.ComponenteDAO;
import styles.GlobalStyles;

public class TelaDashboard extends Application {

    private int posX = 1;
    private int posY = 1;
    private int count = 0;

    //
    private Usuario user;
    private int idMaquina;
    private String descricaoMaquina;
    private List<Componente> cmps;
    private Double leituraComp;

    GridPane gridPane = new GridPane();

    //declaração das labels
    ComponenteDAO cDao = new ComponenteDAO();
    List<Double> somas = new ArrayList<>();

    Integer cont = 1;

    public TelaDashboard(Usuario user, int idMaquina, String descricaoMaquina) {
        this.user = user;
        this.idMaquina = idMaquina;
        this.descricaoMaquina = descricaoMaquina;
    }

    GlobalStyles globalStyles = new GlobalStyles();

    public void looping() {
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                Platform.runLater(() -> {
                    gridPane.getChildren().removeAll();

                    posX = 1;
                    posY = 1;
                    count = 0;

                    for (int i = 0; i < cmps.size(); i++) {
                        leituraComp = cDao.returnLeitura(user.getFkIdFilial(), cmps.get(i).getIdComponente(), idMaquina);
                        Gridpanes gp = new Gridpanes();
                        gp.setLeitura(leituraComp);
                        gp.setSoma(somas.get(i) + leituraComp);
                        somas.set(i, gp.getSoma());
                        gp.calcMedia(cont);
                        gp.medirAlerta(Double.valueOf(cmps.get(i).getTotalComponente()));

                        criarBox(cmps.get(i).getNomeComponente(), gp.getAlerta(), leituraComp, gp.getMedia());

                    }

                    cont++;
                    System.out.println("5 segundos");
                });

            }
        }, 1000, 5000);
    }

    public void criarBox(String nomeComponente, String alerta, Double leitura, Double media) {

        Label lbNomeComponente = new Label();
        Label lbSituacaoComponente = new Label();
        Label lbLeituraAtual = new Label();
        Label lbValorMediaDeUso = new Label();
        Label lbValorLeituraAtual = new Label();
        ProgressBar pb = new ProgressBar();

        lbNomeComponente.setText(nomeComponente);
        lbNomeComponente.setLayoutX(27);
        lbNomeComponente.setLayoutY(17);
        lbNomeComponente.setStyle(globalStyles.getStyleLabels() + "-fx-font: 26 archivo;");

        Label lbComponenteDescricao = new Label();
        lbComponenteDescricao.setLayoutX(lbNomeComponente.getLayoutX() + 60);
        lbComponenteDescricao.setLayoutY(25);
        lbComponenteDescricao.setStyle(globalStyles.getStyleLabels());

        lbSituacaoComponente.setText(String.format("%s em %s", nomeComponente, alerta));
        if (nomeComponente.length() <= 5) {
            lbSituacaoComponente.setLayoutX(390);
        } else {
            lbSituacaoComponente.setLayoutX(330);
        }
        lbSituacaoComponente.setLayoutY(25);
//        if (leitura / 100 <= 0.3) {
////            System.out.println("aqui é verde");
//            lbSituacaoComponente.setStyle(globalStyles.getStyleLabels() + "-fx-text-fill: #0f0");
//        } else if (leitura/100 < 0.7) {
////            System.out.println("aqui é amarelo");
//           lbSituacaoComponente.setStyle(globalStyles.getStyleLabels() + "-fx-text-fill: ff0");
//        } else {
////            System.out.println("aqui é vermelho");
        lbSituacaoComponente.setStyle(globalStyles.getStyleLabels() + "-fx-text-fill: f00");
//        }

        Label lbMediaDeUso = new Label("Média de Uso: ");
        lbMediaDeUso.setLayoutX(lbNomeComponente.getLayoutX());
        lbMediaDeUso.setLayoutY(70);
        lbMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes());

        lbLeituraAtual.setText("Leitura Atual");
        lbLeituraAtual.setLayoutX(lbMediaDeUso.getLayoutX());
        lbLeituraAtual.setLayoutY(100);
        lbLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes());

        lbValorMediaDeUso.setText(media.toString());
        lbValorMediaDeUso.setLayoutX(lbMediaDeUso.getLayoutX() + 140);
        lbValorMediaDeUso.setLayoutY(lbMediaDeUso.getLayoutY());
//         if (leitura / 100 <= 0.3) {
////            System.out.println("aqui é verde");
//            lbValorMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes() + "-fx-text-fill: #0f0");
//        } else if (leitura/100 < 0.7) {
////            System.out.println("aqui é amarelo");
//           lbValorMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes() + "-fx-text-fill: #ff0");
//        } else {
//            System.out.println("aqui é vermelho");
        lbValorMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes() + "-fx-text-fill: #f00");
//        }

        lbValorLeituraAtual.setText(leitura.toString());
        lbValorLeituraAtual.setLayoutX(lbLeituraAtual.getLayoutX() + 130);
        lbValorLeituraAtual.setLayoutY(lbLeituraAtual.getLayoutY());
//        if (leitura/100 <= 0.3) {
////            System.out.println("aqui é verde");
//            lbValorLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes() + "-fx-text-fill: #0f0");
//        } else if (leitura/100 < 0.7) {
////            System.out.println("aqui é amarelo");
//            lbValorLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes() + "-fx-text-fill: #ff0");
//        } else {
//            System.out.println("aqui é vermelho");
        lbValorLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes() + "-fx-text-fill: #f00");
//        }

//        BARRA DE PROGRESSO
        pb.setProgress(leitura / 100);
        pb.setLayoutX(lbNomeComponente.getLayoutX());
        pb.setLayoutY(200);
        pb.setPrefWidth(470);
        pb.prefHeight(30);
        pb.setStyle("-fx-accent: #FF7D7D;");

        Rectangle boxMaquina = new Rectangle(posX, 200, 518, 260);
        boxMaquina.setStyle("-fx-fill: #FFF;");
        boxMaquina.setCursor(Cursor.HAND);
        boxMaquina.setArcHeight(8);
        boxMaquina.setArcWidth(8);

        Pane paneComponente = new Pane();
        paneComponente.setPrefWidth(boxMaquina.getWidth());
        paneComponente.setPrefHeight(boxMaquina.getHeight());

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
        paneComponente.getChildren().add(lbValorMediaDeUso);
        paneComponente.getChildren().add(lbValorLeituraAtual);
        paneComponente.getChildren().add(pb);
    }

    public void start(Stage stage) {
        
        
        ScrollPane scrollPane = new ScrollPane();

        cmps = cDao.returnComponentes(idMaquina);

        Pane pane = new Pane();
        stage.setTitle("Dashboard");
        stage.setResizable(false);
        stage.setScene(new Scene(scrollPane, 1300, 700));
        scrollPane.setContent(pane);

        // HEADER
        Rectangle header = new Rectangle(0, 0, scrollPane.getWidth(), 150);
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
        gridPane.toFront();

        gridPane.setLayoutX(50);
        gridPane.setLayoutY(75);
        gridPane.setHgap(35);
        gridPane.setVgap(35);

//        listaSetores.forEach(s -> {
        cmps.forEach(c -> {

            leituraComp = cDao.returnLeitura(user.getFkIdFilial(), c.getIdComponente(), idMaquina);

            Gridpanes gp = new Gridpanes();

            gp.setLeitura(leituraComp);
            gp.setSoma(gp.getSoma() + leituraComp);
            somas.add(gp.getSoma());
            gp.calcMedia(cont);
            gp.medirAlerta(Double.valueOf(c.getTotalComponente()));

            // Labels dos gridpanes
            criarBox(c.getNomeComponente(), gp.getAlerta(), leituraComp, gp.getMedia());

        });
        cont++;

//        Label lbVelocDown = new Label("Veloc. Down: ");
//        lbVelocDown.setLayoutX(120);
//        lbVelocDown.setLayoutY(675);
//        lbVelocDown.setStyle(globalStyles.getStyleLabels());
//
//        Label lbValorVelocDown = new Label("859KiB/s");
//        lbValorVelocDown.setLayoutX(lbVelocDown.getLayoutX() + 85);
//        lbValorVelocDown.setLayoutY(675);
//        lbValorVelocDown.setStyle(globalStyles.getStyleLabels());
//
//        Label lbVelocUp = new Label("Veloc. Up: ");
//        lbVelocUp.setLayoutX(lbValorVelocDown.getLayoutX() + 90);
//        lbVelocUp.setLayoutY(675);
//        lbVelocUp.setStyle(globalStyles.getStyleLabels());
//
//        Label lbValorVelocUp = new Label("265KiB/s");
//        lbValorVelocUp.setLayoutX(lbVelocUp.getLayoutX() + 70);
//        lbValorVelocUp.setLayoutY(675);
//        lbValorVelocUp.setStyle(globalStyles.getStyleLabels());
//        });
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

//        getChildren veloc down e up
//        pane.getChildren().add(lbVelocDown);
//        pane.getChildren().add(lbValorVelocDown);
//        pane.getChildren().add(lbVelocUp);
//        pane.getChildren().add(lbValorVelocUp);
        stage.show();
        looping();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
