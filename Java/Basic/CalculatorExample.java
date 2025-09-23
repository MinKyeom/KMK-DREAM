package src.Java_Basic;

public class CalculatorExample {
  
  public static void main(String[] args){
    Calculator myCalc = new Calculator(); // 객체 생성
    myCalc.powerOn();

    int result1 = myCalc.plus(5,6);
    System.out.println("result1" + result1);

  }

}
