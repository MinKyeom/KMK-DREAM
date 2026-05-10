public class AnonymousExample {
  public static void main(String[] args){
    Anonymous anony = new Anonymous();

    anony.field2.turnOn();

  // 익명 객체 매개값 사용
  anony.method2(
    new RemoteControl(){
      @Override
      public void turnOn(){
        System.out.println("TV");
      }
      @Override
      public void turnOff(){
        System.out.println("TV OFF");
      }
    }
    
  );
  
  }
  
}
