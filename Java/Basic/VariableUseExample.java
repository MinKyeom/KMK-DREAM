package src.Java_Basic;

public class VariableUseExample {
  public static void main(String[] args){
    int x = 3;
    int y = 5;
    System.out.println(x+" "+y);

    int temp =x;
    x = y;
    y = temp;
    
    System.out.println(x+" "+y);

    // 재정의는 가능
    x = 15;

    System.out.println(x);
  }
  
}

