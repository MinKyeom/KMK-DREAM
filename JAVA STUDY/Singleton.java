public class Singleton {
  private static Singleton singleton = new Singleton();

  private Singleton() {}

  static Singleton getInstance(){
    // 내부라서 static 앞에 클래스 생략되고 바로 쓰는 거 가능 보통은 클래스 이름을 쓰고 접근하는게 맞고 클래스 내부라도 클래스 이름 쓰고 접근은 가능하다
    return singleton; 
  }
}
