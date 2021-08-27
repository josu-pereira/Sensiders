/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jira.clientejira;

import jira.clientejira.ClienteJiraApi;
import jira.clientejira.modelo.Issue;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.IOException;

public class DemoDeUsoClienteApi {

//    public static void main(String[] args) throws IOException {
    public static void abrirChamdo(String nomeComponente, String alerta, String leitura, String nomeUsuario, String maquina) throws IOException {

        // Este "gson" é opcional. Apenas para imprimir os objetos na saÃ­da padrÃ£o, caso queira.
        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        ClienteJiraApi clienteJiraApi = new ClienteJiraApi(
                "sensiders.atlassian.net",
                "201grupo11c@bandtec.com.br",
                "MmpKeqJGyeJmUXOb9DA78ADD"
        );
        try {
            Issue novaIssue = new Issue();
            novaIssue.setProjectKey("CDAT");
            novaIssue.setSummary("Alto uso de "+nomeComponente);
            novaIssue.setDescription(nomeComponente+" chega a "+leitura+" de uso\nUsuário: "+nomeUsuario+"\nMáquina: "+maquina);
            novaIssue.setLabels("alerta");

            clienteJiraApi.criarIssue(novaIssue);
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
