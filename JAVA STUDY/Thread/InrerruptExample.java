package Thread;

public class InrerruptExample {
  public static void main(String[] args){
    Thread thread = new PrintClass2();
    thread.start();

    try{Thread.sleep(1000);} catch(InterruptedException e){}

    thread.interrupt();
  }
  
}
