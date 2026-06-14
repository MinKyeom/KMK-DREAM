package Thread;

public class PrintClass extends Thread{

private boolean stop;

public void setStop(boolean stop){
  this.stop = stop;

}

  @Override
  public void run(){

    while(!stop){
      System.out.println("아직 실행 중");
    }
    // System.out.println("쓰레드");

    System.out.println("이제 멈춤");
  }
}
