public class CarExample {
  public static void main(String[] args){
  //   Car myCar = new Car();

  //   System.out.println(myCar.company);

  //   myCar.keyTurnOn();
  //   myCar.run();

  //   int speed =myCar.getSpeed();
  //   System.out.println("현재 속도"+ speed);

  // Car myCar = new Car();

  // myCar.setSpeed(-50);
  // System.out.println(myCar.getSpeed());

  Car car = new Car();
  

  for(int i =1; i<=5; i++){
    int problemLocation = car.run();

    switch(problemLocation){
      case 1:
        System.out.println("교체");
        car.frontLeftTire = new SonTire("앞",5);
        break;
      
    
      }
    System.out.println("--------경계--------");
  }
  }
}
