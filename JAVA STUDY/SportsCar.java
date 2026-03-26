public class SportsCar extends Car{

//   public void setSpeed(int speed){
//   if(speed < 0){
//     this.speed = 0;
//     return;
//   }
//   else{
//     this.speed = speed;
//   }
// }

// 메소드 선언부는 매개변수를 동일하게 적어줘야한다
  @Override
  public void setSpeed(int speed) { 
    System.out.println("바뀜");
  }

}