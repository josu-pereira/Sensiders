package view;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Cursor;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.shape.*;
import javafx.stage.Stage;
import javax.swing.JOptionPane;
import model.bean.Usuario;
import model.dao.UsuarioDAO;
import styles.GlobalStyles;

public class TelaLogin extends Application {

    private String userEmail;
    private String userPassword;

    GlobalStyles globalStyles = new GlobalStyles();

    public void start(Stage stage) {

        // Layouts
        Pane pane = new Pane();

        stage.setTitle("Login");
        stage.setResizable(false);
        stage.setScene(new Scene(pane, 1300, 700));

        GridPane gridpane = new GridPane();
        gridpane.setLayoutX(495);
        gridpane.setLayoutY(180);
        pane.getChildren().add(gridpane);

        gridpane.setHgap(10);
        gridpane.setVgap(10);

        // HEADER
        Rectangle header = new Rectangle(0, 0, pane.getWidth(), 200);

        // BOX FORM
        Rectangle boxForm = new Rectangle(480, 150, 400, 320);
        boxForm.setStyle("-fx-fill: #FFF;");
        boxForm.setArcHeight(8);
        boxForm.setArcWidth(8);

        // Label
        Label lbTitle = new Label("Login");

        Label lbEmail = new Label("Email");
        Label lbPassword = new Label("Senha");

        // Text Field
        TextField tfEmail = new TextField();
        PasswordField pfPassword = new PasswordField();

        // Button
        Button btnEntrar = new Button("Entrar");
        btnEntrar.setCursor(Cursor.HAND);

        tfEmail.setPrefWidth(350);
        tfEmail.setPrefHeight(35);

        pfPassword.setPrefWidth(tfEmail.getPrefWidth());
        pfPassword.setPrefHeight(tfEmail.getPrefHeight());

        btnEntrar.setPrefWidth(tfEmail.getPrefWidth());
        btnEntrar.setPrefHeight(tfEmail.getPrefHeight());

        // Adicionando os styles
        pane.setStyle(globalStyles.getBackgroundPage());

        header.setStyle(globalStyles.getStyleHeader());

        lbTitle.setStyle(globalStyles.getStyleTitle() + globalStyles.getStyleTitleBlack());
        lbEmail.setStyle(globalStyles.getStyleLabels());
        lbPassword.setStyle(globalStyles.getStyleLabels());

        tfEmail.setStyle(globalStyles.getStyleTextField());
        pfPassword.setStyle(globalStyles.getStyleTextField());

        btnEntrar.setStyle(globalStyles.getStyleButtonConfirm());

        // Adicionando a tela
        pane.getChildren().add(header);
        pane.getChildren().add(boxForm);
        boxForm.toFront();

        gridpane.add(lbTitle, 1, 1);
        gridpane.add(lbEmail, 1, 3);
        gridpane.add(tfEmail, 1, 4);
        gridpane.add(lbPassword, 1, 5);
        gridpane.add(pfPassword, 1, 6);
        gridpane.add(btnEntrar, 1, 8);
        gridpane.toFront();

        // Ações botão
        btnEntrar.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent t) {
                userEmail = tfEmail.getText().trim().toString();
                userPassword = pfPassword.getText().trim().toString();

                if (userEmail.equals("") || userPassword.equals("")) {
                    JOptionPane.showMessageDialog(null, "Opps... Alguns campos estão faltando!", "Erro", JOptionPane.ERROR_MESSAGE);
                } else {

                    Usuario user = UsuarioDAO.login(userEmail, userPassword);

                    if (user == null) {
                        JOptionPane.showMessageDialog(null, "Opps... \n Usuário e/ou senha incorretos!");
                    } else {
                        stage.close();
                        
                        Stage stage = new Stage();
                        new TelaListaMaquinas(user).start(stage);
                        
                        
                        
                        /*
                        TelaDashboard td = new TelaDashboard(user);
                        td.setVisible(true);*/
                    }
                }

            }

        });

        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
