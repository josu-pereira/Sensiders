package view;

/**
 *
 * @author josu, patrick
 */
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.scene.Cursor;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.ScrollPane;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import jira.clientejira.ClienteJiraApi;
import jira.clientejira.DemoDeUsoClienteApi;
import jira.clientejira.modelo.Issue;
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
    private List<Map<String, Object>> leituras;

    ClienteJiraApi clienteJiraApi = new ClienteJiraApi(
            "sensiders.atlassian.net",
            "201grupo11c@bandtec.com.br",
            "MmpKeqJGyeJmUXOb9DA78ADD"
    );

    GridPane gridPane = new GridPane();

    //declaração das labels
    List<Double> somas = new ArrayList<>();

    Integer cont = 1;
    Double auxLeitura = 0.0;

    public TelaDashboard(Usuario user, int idMaquina, String descricaoMaquina) {
        this.user = user;
        this.idMaquina = idMaquina;
        this.descricaoMaquina = descricaoMaquina;
        this.leituras = ComponenteDAO.returnLeitura(this.idMaquina);
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
                        
                        //System.out.println(cmps.get(i).getNomeComponente() + " " + leituras.get(i).get("nome_componente"));
                        for(int j = 0; j < leituras.size(); j++){
                            if(cmps.get(i).getNomeComponente().equals(leituras.get(j).get("nome_componente"))){
                                auxLeitura = Double.valueOf(leituras.get(j).get("leitura").toString());
                                //System.out.println(cmps.get(i).getNomeComponente() + " " + leituras.get(j).get("nome_componente"));
                                break;
                            }    
                        }
                        Gridpanes gp = new Gridpanes();
                        gp.setLeitura(auxLeitura);
                        gp.setSoma(somas.get(i) + auxLeitura);
                        somas.set(i, gp.getSoma());
                        gp.calcMedia(cont);
                        gp.medirAlerta(Double.valueOf(cmps.get(i).getTotalComponente()));

                        criarBox(cmps.get(i).getNomeComponente(), gp);
                        

                    }

                    cont++;
                    System.out.println("5 segundos");
                });

            }
        }, 5000, 5000);
    }

    public void criarBox(String nomeComponente, Gridpanes gp) {

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

        lbSituacaoComponente.setText(String.format("%s em %s", nomeComponente, gp.getAlerta()));
        if (nomeComponente.length() <= 5) {
            lbSituacaoComponente.setLayoutX(390);
        } else {
            lbSituacaoComponente.setLayoutX(330);
        }
        lbSituacaoComponente.setLayoutY(25);
        lbSituacaoComponente.setStyle(globalStyles.getStyleLabels() + gp.getCor());

        Label lbMediaDeUso = new Label("Média de Uso: ");
        lbMediaDeUso.setLayoutX(lbNomeComponente.getLayoutX());
        lbMediaDeUso.setLayoutY(70);
        lbMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes());

        lbLeituraAtual.setText("Leitura Atual");
        lbLeituraAtual.setLayoutX(lbMediaDeUso.getLayoutX());
        lbLeituraAtual.setLayoutY(100);
        lbLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes());

        lbValorMediaDeUso.setText(gp.getMedia().toString());
        lbValorMediaDeUso.setLayoutX(lbMediaDeUso.getLayoutX() + 140);
        lbValorMediaDeUso.setLayoutY(lbMediaDeUso.getLayoutY());
        lbValorMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes() + gp.getCor());

        lbValorLeituraAtual.setText(gp.getLeitura().toString());
        lbValorLeituraAtual.setLayoutX(lbLeituraAtual.getLayoutX() + 130);
        lbValorLeituraAtual.setLayoutY(lbLeituraAtual.getLayoutY());
        lbValorLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes() + gp.getCor());
        if(gp.getAlerta().equals("alto uso")) {
            try {
                //chamado jira
                DemoDeUsoClienteApi.abrirChamdo(lbNomeComponente.getText(), "alto uso", gp.getLeitura().toString(), user.getNomeUsuario(), descricaoMaquina);
            } catch (IOException ex) {
                Logger.getLogger(TelaDashboard.class.getName()).log(Level.SEVERE, null, ex);
            }
        }

//        BARRA DE PROGRESSO
        pb.setProgress(gp.getLeitura() / 100);
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

        cmps = ComponenteDAO.returnComponentes(idMaquina);

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

            //leituraComp = cDao.returnLeitura(user.getFkIdFilial(), c.getIdComponente(), idMaquina);
            for(int i = 0; i< leituras.size(); i++){
                if(leituras.get(i).get("nome_componente").equals(c.getNomeComponente())){
                    auxLeitura = Double.valueOf(leituras.get(i).get("leitura").toString());
                    System.out.println(leituras.get(i).get("nome_componente"));
                    break;
                }
            }
            
            Gridpanes gp = new Gridpanes();

            gp.setLeitura(auxLeitura);
            gp.setSoma(gp.getSoma() + auxLeitura);
            somas.add(gp.getSoma());
            gp.calcMedia(cont);
            gp.medirAlerta(Double.valueOf(c.getTotalComponente()));
            System.out.println(auxLeitura);

            criarBox(c.getNomeComponente(), gp);
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
