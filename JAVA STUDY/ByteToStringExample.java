import java.lang.*;

public class ByteToStringExample {
  public static void main(String[] args){
    byte[] bytes ={72,101,108};

    String str1 = new String(bytes);
    System.out.println(str1);

    String str2 = new String(bytes,0,2);
    System.out.println(str2);

  }
  
}
