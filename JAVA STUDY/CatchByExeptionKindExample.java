public class CatchByExeptionKindExample {

  public static void main (String[] args){
    try{
      String data1 = args[0];
      String data2 = args[1];
      int value1 = Integer.parseInt(data1);
      int value2 = Integer.parseInt(data2);
      System.out.println("result");
    }catch(ArrayIndexOutOfBoundsException e){
      System.out.println("error");
    }

    try{
      String data1 = args[0];    
    }catch(NumberFormatException e ){
      System.out.println("error2");
    }finally{
      System.out.println("error3");
    }

  
  }
  
}
