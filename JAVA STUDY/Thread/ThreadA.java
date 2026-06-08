package Thread;

public class ThreadA extends Thread {
  public ThreadA() {
    setName("ThreadA");
  }
  
  @Override
  public void run(){
    System.out.println("ThreadA!!");
  }

  
}
