public class AnimalExample {
  public static void main(String[] args){
    Dog dog = new Dog();

    dog.sound();
  
    System.out.println("---");
    
    Animal animal = null;
    animal = new Dog();
    animal.sound();

    System.out.println("---");

    animalSound(new Dog());
  }

    public static void animalSound(Animal animal){
      animal.sound();
    }
}
