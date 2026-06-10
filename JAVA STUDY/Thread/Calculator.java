package Thread;

public class Calculator {

  private int memory;

  public int getMemory(){
    return memory;
  }

  
  // public void setMemory(int memory){
  // 동기화 메서드를 부여후 메소드 잠금 기능 추가
  public synchronized void setMemory(int memory){
    this.memory = memory;

    try{
      Thread.sleep(2000);

    }catch(InterruptedException e){}
    System.out.println(Thread.currentThread().getName() + ": " + this.memory);
  }
  
}
