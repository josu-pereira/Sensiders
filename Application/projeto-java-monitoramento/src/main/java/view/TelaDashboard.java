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
import javax.swing.JOptionPane;
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
    List<List<Double>> last = new ArrayList<>();

    Integer contLast = 0;
    Integer cont = 1;
    Double auxLeitura = 0.0;
    String auxString = "";

    public TelaDashboard(Usuario user, int idMaquina, String descricaoMaquina) {
        this.user = user;
        this.idMaquina = idMaquina;
        this.descricaoMaquina = descricaoMaquina;
        this.leituras = ComponenteDAO.returnLeitura2(this.idMaquina);
    }

    GlobalStyles globalStyles = new GlobalStyles();
    Timer timer = new Timer();

    public void looping() {

        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                Platform.runLater(() -> {
                    gridPane.getChildren().removeAll();
                    leituras = ComponenteDAO.returnLeitura2(idMaquina);

                    posX = 1;
                    posY = 1;
                    count = 0;
                    System.out.println(last);

                    for (int i = 0; i < cmps.size(); i++) {

                        //System.out.println(cmps.get(i).getNomeComponente() + " " + leituras.get(i).get("nome_componente"));
                        for (int j = 0; j < leituras.size(); j++) {
                            if (cmps.get(i).getNomeComponente().equals(leituras.get(j).get("nome_componente"))) {
                                auxLeitura = Double.valueOf(leituras.get(j).get("leitura").toString());
                                //System.out.println(cmps.get(i).getNomeComponente() + " " + leituras.get(j).get("nome_componente"));
                                break;
                            }
                        }

                        Gridpanes gp = new Gridpanes();
                        gp.setNome(cmps.get(i).getNomeComponente());
                        gp.setLeitura(auxLeitura);
                        last.get(i).add(auxLeitura);
                        gp.setSoma(somas.get(i) + auxLeitura);
                        somas.set(i, gp.getSoma());
                        gp.calcMedia(cont);
                        gp.medirAlerta();

                        criarBox(gp);
                    }
                    
                    for (int k = 0; k < last.size(); k++) {
                            contLast = 0;
                            for (int l = 0; l < last.get(k).size(); l++) {
                                auxString = String.valueOf(last.get(k).get(l));
                                if (Double.valueOf(auxString) >= 70) {
                                    contLast++;
                                    if(cmps.get(k).getNomeComponente().equalsIgnoreCase("cpu") || cmps.get(k).getNomeComponente().equalsIgnoreCase("ram")
                                            || cmps.get(k).getNomeComponente().equalsIgnoreCase("hd")|| cmps.get(k).getNomeComponente().equalsIgnoreCase("temperatura")){
                                        if(contLast>=5){
                                            last.get(k).removeAll(last.get(k));
                                            try {
                                                DemoDeUsoClienteApi.abrirChamdo(cmps.get(k).getNomeComponente(), "alto uso", leituras.get(k).get("leitura").toString(), user.getNomeUsuario(), descricaoMaquina);
                                                JOptionPane.showMessageDialog(null, "Opps... O componente " + cmps.get(k).getNomeComponente() + " está tendo um alto uso, abriremos um chamado", "Atenção", JOptionPane.WARNING_MESSAGE);
                                            } catch (IOException ex) {
                                                Logger.getLogger(TelaDashboard.class.getName()).log(Level.SEVERE, null, ex);
                                            }
                                        }
                                    }
                                }
                            }
                        }

                    cont++;
                    System.out.println("10 segundos");
                });

            }
        }, 2000, 10000);
    }

    public void criarBox(Gridpanes gp) {

        Label lbNomeComponente = new Label();
        Label lbSituacaoComponente = new Label();
        Label lbLeituraAtual = new Label();
        Label lbValorMediaDeUso = new Label();
        Label lbValorLeituraAtual = new Label();
        ProgressBar pb = new ProgressBar();

        lbNomeComponente.setText(gp.getNome());
        lbNomeComponente.setLayoutX(27);
        lbNomeComponente.setLayoutY(17);
        lbNomeComponente.setStyle(globalStyles.getStyleLabels() + "-fx-font: 26 archivo;");

        Label lbComponenteDescricao = new Label();
        lbComponenteDescricao.setLayoutX(lbNomeComponente.getLayoutX() + 60);
        lbComponenteDescricao.setLayoutY(25);
        lbComponenteDescricao.setStyle(globalStyles.getStyleLabels());

        lbSituacaoComponente.setText(String.format("%s em %s", gp.getNome(), gp.getAlerta()));
        Integer tamanhoComponente = gp.getNome().length();
        switch (tamanhoComponente) {
            case 2:
                lbSituacaoComponente.setLayoutX(380);
                break;
            case 3:
                lbSituacaoComponente.setLayoutX(380);
                break;
            case 4:
                lbSituacaoComponente.setLayoutX(380);
                break;
            case 5:
                lbSituacaoComponente.setLayoutX(380);
                break;
            case 6:
                lbSituacaoComponente.setLayoutX(350);
                break;
            case 7:
                lbSituacaoComponente.setLayoutX(350);
                break;
            case 8:
                lbSituacaoComponente.setLayoutX(330);
                break;
            case 11:
                lbSituacaoComponente.setLayoutX(300);
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

        lbValorMediaDeUso.setText(String.format("%.2f", gp.getMedia()));
        lbValorMediaDeUso.setLayoutX(lbMediaDeUso.getLayoutX() + 140);
        lbValorMediaDeUso.setLayoutY(lbMediaDeUso.getLayoutY());
        lbValorMediaDeUso.setStyle(globalStyles.getStyleLabelsComponentes() + gp.getCor());

        lbValorLeituraAtual.setText(gp.getLeitura().toString());
        lbValorLeituraAtual.setLayoutX(lbLeituraAtual.getLayoutX() + 130);
        lbValorLeituraAtual.setLayoutY(lbLeituraAtual.getLayoutY());
        lbValorLeituraAtual.setStyle(globalStyles.getStyleLabelsComponentes() + gp.getCor());

//        BARRA DE PROGRESSO
        if (gp.getNome().equals("UPLOAD") || gp.getNome().equals("DOWNLOAD") || gp.getNome().equals("TASKS")) {
            pb.setVisible(false);
        } else {
            pb.setProgress(gp.getLeitura() / 100);
            pb.setLayoutX(lbNomeComponente.getLayoutX());
            pb.setLayoutY(200);
            pb.setPrefWidth(470);
            pb.prefHeight(30);
            pb.setStyle("-fx-accent: #FF7D7D;");
        }

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
            for (int i = 0; i < leituras.size(); i++) {
                if (leituras.get(i).get("nome_componente").equals(c.getNomeComponente())) {
                    auxLeitura = Double.valueOf(leituras.get(i).get("leitura").toString());
                    //System.out.println(leituras.get(i).get("nome_componente"));
                    break;
                }
            }

            Gridpanes gp = new Gridpanes();

            gp.setNome(c.getNomeComponente());
            gp.setLeitura(auxLeitura);
            gp.setSoma(gp.getSoma() + auxLeitura);
            somas.add(gp.getSoma());
            gp.calcMedia(cont);
            gp.medirAlerta();
            System.out.println(auxLeitura);
            List<Double> auxLast = new ArrayList<>();
            auxLast.add(auxLeitura);
            last.add(auxLast);

            criarBox(gp);
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
                stage.close();
                Stage stage = new Stage();
                new TelaListaMaquinas(user).start(stage);
                timer.cancel();
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
