class DoubleThreadTest1 extends Thread {
  public DoubleThreadTest1(String str) {
    setName(str);
  }
  public void run() {
    for (int i=1 ; i<=3 ; i++) {
       System.out.println(i + getName());
    }	
    System.out.println("끝" + getName());
  }
}
public class DoubleThread1 {
  public static void main(String args[]) {
    DoubleThreadTest1 t1 = new DoubleThreadTest1(" : 배우기 쉬운 자바");
    DoubleThreadTest1 t2 = new DoubleThreadTest1(" : 배우기 어려운 자바");
    System.out.println("***** 스레드 시작 전 *****");
    t1.start();
    t2.start();
    System.out.println("***** 스레드 종료 후 *****");
  }
}
