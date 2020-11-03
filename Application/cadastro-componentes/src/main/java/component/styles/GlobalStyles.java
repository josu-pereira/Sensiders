package component.styles;

public class GlobalStyles {
    
    private String styleHeader = "-fx-fill: #FF7D7D";
    private String backgroundPage = "-fx-background-color: #e6e6e6";
    
   
    private String styleTextField = "-fx-background-color: #FAFAFA;"
            + "-fx-border-radius: 8; -fx-font: 14 poppins;";
    
    private String styleButtonConfirm = "-fx-background-color: #7DFB91; -fx-font: 14 poppins ;"
            + "-fx-border-radius: 8; -fx-text-fill: #FFF;  -fx-font-weight: bold";
    
    public String styleTitle = "-fx-font: 18 archivo;";
  
    public String styleErrorMessage = "-fx-font: 14 poppins; -fx-font-weight: bold;"
            + "-fx-text-fill: #F00";
    
    
    public String getStyleTitle() {
        return styleTitle;
    }

    public String getStyleErrorMessage() {
        return styleErrorMessage;
    }
    
    
    
    
    public String getBackgroundPage() {
        return backgroundPage;
    }

    public String getStyleHeader() {
        return styleHeader;
    }

    public String getStyleTextField() {
        return styleTextField;
    }

    public String getStyleButtonConfirm() {
        return styleButtonConfirm;
    }
}
