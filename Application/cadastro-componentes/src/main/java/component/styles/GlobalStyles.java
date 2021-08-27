package component.styles;

public class GlobalStyles {
    
    private String styleHeader = "-fx-fill: #FF7D7D";
    private String backgroundPage = "-fx-background-color: #e6e6e6";
    
   
    private String styleTextField = "-fx-background-color: #FAFAFA;"
            + "-fx-border-radius: 8; -fx-font: 14 poppins;";
    
    private String styleButtonConfirm = "-fx-background-color: #7DFB91; -fx-font: 14 poppins ;"
            + "-fx-border-radius: 8; -fx-text-fill: #FFF;  -fx-font-weight: bold";
    
    public String styleErrorMessage = "-fx-font: 14 poppins; -fx-font-weight: bold;"
            + "-fx-text-fill: #F00";
    private String styleLabels = "-fx-font: 14 archivo;";
    
    public String styleTitle = "-fx-font: 18 archivo; -fx-font-weight: bold; "
            + "-fx-text-fill: #FFF;";
    
    public String styleTitleBlack = "-fx-text-fill: #000";

    public String getStyleTitleBlack() {
        return styleTitleBlack;
    }
    
    public String styleTfSearch = "-fx-background-color: #FAFAFA;"
            + "-fx-border-radius: 8; -fx-font: 14 poppins; -fx-text-fill: gray";

    public String getStyleTfSearch() {
        return styleTfSearch;
    }

    public String getStyleLabels() {
        return styleLabels;
    }
    
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
