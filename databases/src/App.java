import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class App{
    public static void main(String[] args) {
        try {
            Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/my_web_data","root","Firewar@@2022");
            if(conn!=null){
                System.out.println("Connection Successful...");
            }
            Statement st=conn.createStatement();
              
             //decisiontree prediction confusionmatrix
            st.executeUpdate("insert into decision_tree_cn values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\tree\\cn.png');");
            //decisionTreeClassifier,ababoosting, gradientboosting
            st.executeUpdate("insert into decision_tree values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\tree\\dt.png','C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\ada\\adt.png','C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\gradient\\gt.png');");
            //pca
            st.executeUpdate("insert into pca values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\pca\\n" + //
                                "_feature_pred\\psdt.png','pca/pca_an/pcadt.png');");
            // random_forest_cn
            st.executeUpdate("insert into random_forest_cn values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\cn.png');");
            
           //random_forest_classifier
           st.executeUpdate("insert into random_forest values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\rfc1.png'),(2,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\rfc2.png'),(3,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\rfc3.png');");
           
          // BaggingClassifer
            st.executeUpdate("insert into bagging values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\baggingclassifier\\bcdt.png');");
            //Stacking logisticRegression, StackingClassifier
            st.executeUpdate("insert into stacking values(1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\logistic_regression\\lrcount.png','C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\stackingclassifier\\stackclass-pdt.png'); ");
            //stacking votingClassifier
            st.executeUpdate("insert into voting values (1,'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\votingclassifier\\voting(hard)-count.png','C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\votingclassifier\\voting(soft)-pbd.png');");
        
           System.out.println("data saved successfully");
            conn.close();
        
        } catch (SQLException e) {
        }
        
    }
}