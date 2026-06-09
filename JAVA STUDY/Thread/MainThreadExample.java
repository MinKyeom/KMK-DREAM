package Thread;

public class MainThreadExample {

  public static void main(String[] args){
    Calculator Calculator = new Calculator();

    User1 user1 = new User1();
    user1.setCalculator(Calculator);
    user1.start();

    User2 user2 = new User2();
    user2.setCalculator(Calculator);
    user2.start();


  }
  
}
