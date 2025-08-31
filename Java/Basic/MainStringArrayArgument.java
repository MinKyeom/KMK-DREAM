// 실행 명령어 :  javac -d out src/Java_Basic/MainStringArrayArgument.java
// 실행 명령어 : java -cp out src.Java_Basic.MainStringArrayArgument 10 20 

// 인자 넘겨주는 방식 

package src.Java_Basic;

public class MainStringArrayArgument {
  public static void main(String[] args){
    if(args.length != 2){
      System.out.println("값의 수가 부족합니다");
      System.exit(0);
    
    }
    String strNum1 = args[0];
    String strNum2 = args[1];

    System.out.println("나오나?");
  }
  
}
