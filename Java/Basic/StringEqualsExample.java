package src.Java_Basic;

public class StringEqualsExample {
  public static void main(String[] args){

    String strVar1 = "check1";
    String strVar2 = "check1";

    // 참조 주소로 확인
    if(strVar1==strVar2){
      System.out.println("strVal과 strVal2 참조 같음");
    }
    else{
      System.out.println("같지 않음");
    }

    if(strVar1.equals(strVar2)){
      System.out.println("역시 같군");
    }

    String strVar3 = new String("check1");
    String strVar4 = new String("check1");

    if(strVar3 == strVar4 ){
      System.out.println("새로운 객체도 같아");
    }
    else{
      System.out.println("새로운 객체는 달라");
    }

    if(strVar3.equals(strVar4)){
      System.out.println("equals는 같아");
    }

  }
}
