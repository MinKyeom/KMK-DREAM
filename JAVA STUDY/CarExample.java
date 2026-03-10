public class CarExample {
  public static void main(String[] args){
    Car myCar = new Car();

    System.out.println(myCar.company);

    myCar.keyTurnOn();
    myCar.run();

    int speed =myCar.getSpeed();
    System.out.println("현재 속도"+ speed);
  }
}
