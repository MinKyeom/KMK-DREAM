package Thread;

public class SleepExample {

  public static void main(String[] args){
    PrintClass print = new PrintClass();
    
    try{
      Thread.sleep(3000);
      System.out.println("3초 지남");
    }catch(InterruptedException e){}
  
    print.run();
  }
  
  

}
