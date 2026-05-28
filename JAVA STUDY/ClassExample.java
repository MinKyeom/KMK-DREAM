public class ClassExample {

  public static void main(String[] args) throws Exception{
    // 클래스로부터 얻는 방법
    Class clazz = Car.class;

    Class clazz2 = Class.forName("");

    //객체로부터 얻는 방법
    Car car = new Car();
    Class clazz3 = car.getClass();

  }
  
}
