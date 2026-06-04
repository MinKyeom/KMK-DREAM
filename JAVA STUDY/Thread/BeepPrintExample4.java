package Thread;

public class BeepPrintExample4 {
  public static void main(String[] args){
    Thread thread = new PrintClass();
    thread.start();

    System.out.println("메인쓰레드");
  }
}
