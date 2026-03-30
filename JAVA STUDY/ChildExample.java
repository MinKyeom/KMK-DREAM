public class ChildExample {
  public static void main(String[] args){

    // 자식 객체 생성
    Child child = new Child();

    // 자식 객체의 부모 객체의 타입으로 변경
    Parent parent = child;
    // 자식 객체에 오버라이딩 된 거 없는 method1은 부모에서 가져옴
    parent.method1();
    // 자식 객체에 오버라이딩 된 거 있고 method2도 부모 객체에 있음
    // 자식 객체의 오버라이딩 된 메소드로 불러옴
    parent.method2();

    // 부모 객체로 변경된 순간부터 못씀 부모 객체에는 없기 때문에
    // 자식 객체에만 존재해서 못불러옴
    // parent.method3();
  }
}
