import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ELT_Study {
    public static void main(String[] args) throws Exception {
        String sourceUrl = "jdbc:postgresql://source_host/db";
        String targetUrl = "jdbc:postgresql://target_host/dw";
        
        List<Order> extractedData = new ArrayList<>();

        // 1. Extract: 소스 DB에서 데이터 읽기
        try (Connection srcConn = DriverManager.getConnection(sourceUrl, "user", "pass");
             Statement stmt = srcConn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT id, name, amount FROM orders")) {
            
            while (rs.next()) {
                extractedData.add(new Order(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getDouble("amount")
                ));
            }
        }

        // 2. Transform: 자바 애플리케이션 내에서 데이터 변환 (소문자 -> 대문자)
        for (Order order : extractedData) {
            order.setName(order.getName().toUpperCase());
        }

        // 3. Load: 변환된 데이터를 타겟 데이터 웨어하우스에 적재
        try (Connection tgtConn = DriverManager.getConnection(targetUrl, "user", "pass");
             PreparedStatement pstmt = tgtConn.prepareStatement("INSERT INTO fact_orders (id, name, amount) VALUES (?, ?, ?)")) {
            
            for (Order order : extractedData) {
                pstmt.setInt(1, order.getId());
                pstmt.setString(2, order.getName());
                pstmt.setDouble(3, order.getAmount());
                pstmt.addBatch();
            }
            pstmt.executeBatch();
        }
    }
    
    // 단순 DTO 클래스
    static class Order {
        private int id; private String name; private double amount;
        public Order(int id, String name, double amount) { this.id = id; this.name = name; this.amount = amount; }
        public int getId() { return id; }
        public String getName() { return name; }
        public void setName(String name) { this.name = name; }
        public double getAmount() { return amount; }
    }
}