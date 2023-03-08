class ThreadTest extends Thread {
  public void run() {
      for (int i=1 ; i<=10 ; i++) {
         System.out.println("재미있는 자바 :" + i);
      }
  }
}
public class ThreadFromThread {
  public static void main(String args[]) {
    ThreadTest t = new ThreadTest();     
    t.start();
   }
}