public class ThrowsExample {
  public static void main(String[] args){
    try{
      findClass();

    }catch(ClassNotFoundException e){
      System.out.println("클래스 없음");
    }
  }
  
  public static void findClass() throws ClassNotFoundException{
    Class clazz = Class.forName("java.lang.String2");
  }
}
