package src.Java_Basic;

public class Car {
  String company ="현대자동차";
  // String model = "그랜저";
  // String color = "검정";
  String model;
  String color;
  int maxSpeed;

  // int maxSpeed = 350;
  int speed;   

  // 중복 코드 제거 전
  // Car(){
    
  // }
  // Car(String model){
  //   this.model = model;
  // }
  
  // Car(String model, String color, int maxSpeed){
  //   this.model = model;
  //   this.color = color;
  //   this.maxSpeed = maxSpeed;
  // }
  // Car(String color, int cc){

  // }

  // 중복 코드 제거 후 

  Car(){
  }

  Car(String model){
    this(model,"은색", 250);
  }

  Car(String model, String color){
    this(model,color,250);
  }

  Car(String model, String color, int maxSpeed){
    this.model = model;
    this.color = color;
    this.maxSpeed = maxSpeed;
  }
}

