import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DBConnection {

    private static HikariDataSource dataSource;

    // 1. 초기화 블록에서 커넥션 풀(DataSource) 설정
    static {
        try {
            HikariConfig config = new HikariConfig();
            config.setJdbcUrl("jdbc:mysql://localhost:3306/my_database");
            config.setUsername("user");
            config.setPassword("password");
            config.setDriverClassName("com.mysql.cj.jdbc.Driver");

            // HikariCP 성능 및 풀 세부 설정
            config.setMaximumPoolSize(10);        // 최대 커넥션 개수
            config.setMinimumIdle(5);             // 최소 유지 유휴 커넥션 개수
            config.setConnectionTimeout(30000);   // 커넥션 획득 대기 타임아웃 (30초)
            config.setIdleTimeout(600000);        // 유휴 커넥션 폐기 시간 (10분)

            dataSource = new HikariDataSource(config);
        } catch (Exception e) {
            System.err.println("HikariCP 초기화 실패: " + e.getMessage());
            throw new RuntimeException(e);
        }
    }

    // 2. 커넥션 풀에서 커넥션을 대여하는 메서드
    public static Connection getConnection() throws SQLException {
        return dataSource.getConnection();
    }

    // 3. 실제 사용 예시 (Try-with-resources 문법으로 자원 자동 반환)
    public static void main(String[] args) {
        String sql = "SELECT 1";

        // Connection, PreparedStatement, ResultSet을 try문 괄호 안에 선언하면 
        // 작업 완료 후 역순으로 .close()가 자동 호출됩니다. (메모리 누수 방지)
        try (Connection conn = DatabaseManager.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            if (rs.next()) {
                int result = rs.getInt(1);
                System.out.println("Connection Success! Result: " + result);
            }

        } catch (SQLException e) {
            System.err.println("SQL 실행 중 에러 발생: " + e.getMessage());
            e.printStackTrace();
        }
    }
}