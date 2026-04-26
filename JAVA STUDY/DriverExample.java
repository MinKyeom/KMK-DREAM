public class DriverExample {
  public static void main(String[] args){
    Driver driver = new Driver();

    Bus bus = new Bus();
    // Taxi taxi = new Taxi();

    // 자동타입 변환
    driver.drive(bus);
    // driver.drive(taxi);

  }
}
