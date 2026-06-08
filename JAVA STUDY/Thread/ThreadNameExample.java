package Thread;

public class ThreadNameExample {

  public static void main(String[] args){
    Thread mainThread = Thread.currentThread();
    System.out.println("메인"+ mainThread.getName());

    ThreadA threadA = new ThreadA();
    System.out.println("서브"+threadA.getName());  

  }
}
