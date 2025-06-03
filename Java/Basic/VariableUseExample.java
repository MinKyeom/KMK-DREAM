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

    x = 15;

    System.out.println(x);
  }
  
}

