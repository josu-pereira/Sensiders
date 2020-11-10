/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jira.clientejira.modelo;

public class IssueField {

    protected String id;
    protected String key;
    protected String name;

    public IssueField(Long id) {
        this.id = id.toString();
    }

    public IssueField(String key) {
        this.key = key;
    }

    public String getId() {
        return id;
    }

    public String getKey() {
        return key;
    }

    public String getName() {
        return name;
    }
}