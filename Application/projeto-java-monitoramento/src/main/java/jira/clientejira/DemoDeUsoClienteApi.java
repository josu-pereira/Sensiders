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

    public static void main(String[] args) throws IOException {

        // Este "gson" Ã© opcional. Apenas para imprimir os objetos na saÃ­da padrÃ£o, caso queira.
        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        ClienteJiraApi clienteJiraApi = new ClienteJiraApi(
                "sensiders.atlassian.net",
                "201grupo11c@bandtec.com.br",
                "MmpKeqJGyeJmUXOb9DA78ADD"
        );
//        System.out.println(gson.toJson(clienteJiraApi));;;
        
//        Issue issue = clienteJiraApi.getIssue("CDAT-1");;
//        System.out.println("Issue recuperada: "+gson.toJson(issue));

        // Exemplo de objeto para novo chamado (Issue)
        Issue novaIssue = new Issue();
        novaIssue.setProjectKey("CDAT");
        novaIssue.setSummary("Alto uso de ram");
        novaIssue.setDescription("RAM chega a 90% de uso");
        novaIssue.setLabels("alerta-cpu", "alerta-disco");

        clienteJiraApi.criarIssue(novaIssue);
        //System.out.println("Issue criada: "+gson.toJson(novaIssue));
//        System.out.println(gson.toJson(clienteJiraApi));
    }
}
