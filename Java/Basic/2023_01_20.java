package src.Java_Basic;

class Parent {
  int x = 1000;
  Parent() {
    this(3000);
  }
  Parent(int x){
    this.x = x;
  }
}

class Child extends Parent{
  int x = 4000;
  Child() {
    this(5000);
  }

  Child(int x){
    this.x =x;
  }
  int getX() {
    return this.x
  }
}

public class 2023_01_20 {
  public static void main(String[] args){
    Child c = new Child();
    System.out.println(c.getX());
  }
  
}
