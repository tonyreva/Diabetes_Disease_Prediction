
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class Table {
    public static void main(String[] args) {
        try {
            Connection connection=DriverManager.getConnection("jdbc:mysql://localhost:3306/my_web_data","root","Firewar@@2022");
                if(connection!=null){
                    System.out.println("conn");
                }
            Statement st=connection.createStatement();
            ResultSet rs=st.executeQuery("show tables;");
            System.out.println(rs.next());
            while(rs.next()){
                System.out.println(rs.getString(1));
            }


        } catch (SQLException e) {
        }
    }
}
