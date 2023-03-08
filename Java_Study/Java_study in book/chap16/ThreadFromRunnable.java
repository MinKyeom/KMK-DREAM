class RunnableTest implements Runnable {
  public void run() {
    for (int i=1 ; i<=10 ; i++) {
      System.out.println("재미있는 자바 :" + i);
    }
  }	
}
public class ThreadFromRunnable {
  public static void main(String args[]) {
    RunnableTest r = new RunnableTest();
    Thread t = new Thread(r);
    t.start();
  }
}

