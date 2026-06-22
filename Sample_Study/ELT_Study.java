import java.sql.*;

public class ELT_Study {
    public static void main(String[] args) throws Exception {
        String sourceUrl = "jdbc:postgresql://source_host/db";
        String targetUrl = "jdbc:postgresql://target_host/dw";

        // 1 & 2. Extract & Load: 소스에서 읽어와 변환 없이 타겟의 Staging 테이블로 바로 스트리밍 적재
        try (Connection srcConn = DriverManager.getConnection(sourceUrl, "user", "pass");
             Connection tgtConn = DriverManager.getConnection(targetUrl, "user", "pass");
             Statement srcStmt = srcConn.createStatement();
             ResultSet rs = srcStmt.executeQuery("SELECT id, name, amount FROM orders");
             PreparedStatement tgtPstmt = tgtConn.prepareStatement("INSERT INTO stg_orders (id, name, amount) VALUES (?, ?, ?)")) {
            
            while (rs.next()) {
                tgtPstmt.setInt(1, rs.getInt("id"));
                tgtPstmt.setString(2, rs.getString("name")); // 변환 없이 그대로 입력
                tgtPstmt.setDouble(3, rs.getAmount());
                tgtPstmt.addBatch();
            }
            tgtPstmt.executeBatch();
        }

        // 3. Transform: 타겟 데이터 웨어하우스 내부에서 SQL(UPPER 함수)을 통해 변환 후 최종 테이블로 이동
        try (Connection tgtConn = DriverManager.getConnection(targetUrl, "user", "pass");
             Statement tgtStmt = tgtConn.createStatement()) {
            
            String transformSql = 
                "INSERT INTO fact_orders (id, name, amount) " +
                "SELECT id, UPPER(name), amount FROM stg_orders";
                
            tgtStmt.executeUpdate(transformSql);
        }
    }
}
