package Thread;

public class BeepPrintExample5 {
  public static void main(String[] args){
    Thread thread = new Thread(){
      @Override
      public void run(){
        System.out.println("서브 쓰레드");
      }
    };
    thread.start();

    System.out.println("메인쓰레드");
  }
  
}
