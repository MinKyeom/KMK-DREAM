public class Car {
//   String company = "현대 자동차";
//   String model = "그랜저";
//   String color = "검정";
//   int maxSpeed = 350;
//   int speed;

//   // 생성자
//   Car(){

//   }

//   Car(String model){
//     this.model = model;
//   }

//   Car(String model , String color){
//     this.model =model;
//     this.color =color;
//   }


// // 메소드 
// int getSpeed(){
//   return speed;
// }

// void keyTurnOn(){
//   System.out.println("키를 돌립니다");
// }

// void setSpeed(int speed){
//   this.speed = speed;
// }

// void run(){
//   for(int i = 0; i <= 1; i+=1){
//     this.setSpeed(i);
//     System.out.println("달립니다."+speed);
//   }
// }

// public static void main(String[] args){
//   Car myCar = new Car();
//   myCar.speed = 60;

//   myCar.run();
// }


// private int speed;
// private boolean stop;

// public int getSpeed(){
//   return speed;
// }

// public void setSpeed(int speed){
//   if(speed < 0){
//     this.speed = 0;
//     return;
//   }
//   else{
//     this.speed = speed;
//   }
// }

// public boolean isStop(){
//   return stop;
// }
// public void setStop(boolean stop){
//   this.stop = stop;
//   this.speed = 0 ;
// }

// public final void stop() {
//   System.out.println("차를 멈춤");
//   speed = 0;
// }

Tire frontLeftTire = new Tire("앞왼쪽",6);
Tire frontRightTire = new Tire("앞오른쪽",2);
Tire backLeftTire = new Tire("뒤왼쪽",3);

}
