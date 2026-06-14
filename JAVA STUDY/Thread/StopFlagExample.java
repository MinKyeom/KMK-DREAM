package Thread;

public class StopFlagExample {
  public static void main(String[] args){


    PrintClass printThread = new PrintClass();

    printThread.start();

    try{ Thread.sleep(1000);} catch(InterruptedException e ){}

    printThread.setStop(true);

  }
  
}
