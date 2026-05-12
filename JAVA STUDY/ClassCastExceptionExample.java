public class ClassCastExceptionExample {

  public static void main(String[] args){
    Dog dog = new Dog();
    changeDog(dog);
  
  
  }
  
  public static void changeDog(Animal animal){
    if(animal instanceof Dog){
    Dog dog = (Dog) animal;
  }
 }
}
