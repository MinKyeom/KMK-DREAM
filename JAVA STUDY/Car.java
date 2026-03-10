public class Car {
  String company = "현대 자동차";
  String model = "그랜저";
  String color = "검정";
  int maxSpeed = 350;
  int speed;

  // 생성자
  Car(){

  }

  Car(String model){
    this.model = model;
  }

  Car(String model , String color){
    this.model =model;
    this.color =color;
  }


// 메소드 
int getSpeed(){
  return speed;
}

void keyTurnOn(){
  System.out.println("키를 돌립니다");
}

void run(){
  for(int i = 0; i <= 50; i+=0){
    speed = i;
    System.out.println("달립니다."+speed);
  }
}

}
