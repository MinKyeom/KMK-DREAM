// 매개변수의 인터페이스화
public class Driver {

  // public void drive(Vehicle vehicle){
  //   vehicle.run();
  // }
  
  public void drive(Vehicle vehicle){
    if(vehicle instanceof Bus){
      Bus bus = (Bus) vehicle;
      bus.checkFare();
    }

    vehicle.run();
  }
}
