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


 // 익명 구현 객체 생성
  RemoteControl field2 = new RemoteControl(){
    @Override
    public void turnOn(){
      System.out.println("Tv On");
    }

    @Override
    public void turnOff(){
      System.out.println("Tv Off");
    }
  };

}
