package src.Java_Basic;
import src.Java_Basic.Car;

public class CarExample {
  public static void main(String[] args){
  Car myCar = new Car(); // 객체 생성

  System.out.println("제작회사"+ myCar.company);
  System.out.println(myCar.model);

  System.out.println("현재 속도:"+ myCar.speed);

  myCar.speed = 60;

  System.out.println("수정된 속도:"+ myCar.speed);
}

}
