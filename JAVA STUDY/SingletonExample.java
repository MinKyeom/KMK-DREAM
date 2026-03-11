public class SingletonExample {
  public static void main(String[] args){
    /*
     컴파일 에러 발생 예시
     * Singleton obj1 = new Singleton();
     * Singleton obj2 = new Singleton(); 
     */

    Singleton obj1 = Singleton.getInstance();
    Singleton obj2 = Singleton.getInstance();

    if(obj1 == obj2){
      System.out.println("같은 객체 입니다");
    }
    else{
      System.out.println("다릅니다");
    }
  } 
}
