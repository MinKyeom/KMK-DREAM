package Thread;

public class PrintClass2 extends Thread {

  public void run(){
    // try{
      while(true){
        System.out.println("실행");
        // Thread.sleep(1); 

        if(Thread.interrupted()){
        break;
        }
      // }
    // }catch(InterruptedException e){}

    System.out.println("자원 정리 후 종료");
    }
  }
}
