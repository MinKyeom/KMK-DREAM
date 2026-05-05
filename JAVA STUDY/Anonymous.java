public class Anonymous {

  Person field =new Person(){
    void work(){
      System.out.println("출근");
    }

    @Override
    void wake(){
      System.out.println("6");
      work();
    }

  };

  

  
}
