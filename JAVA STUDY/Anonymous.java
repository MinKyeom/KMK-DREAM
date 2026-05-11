// public class Anonymous {

//   Person field =new Person(){
//     void work(){
//       System.out.println("출근");
//     }

//     @Override
//     void wake(){
//       System.out.println("6");
//       work();
//     }

//   };


//  // 익명 구현 객체 생성
//   RemoteControl field2 = new RemoteControl(){
//     @Override
//     public void turnOn(){
//       System.out.println("Tv On");
//     }

//     @Override
//     public void turnOff(){
//       System.out.println("Tv Off");
//     }
//   };

//   void method2(RemoteControl rc){
//     rc.turnOn();
//     }
//   }

public class Anonymous {
  private int field;
  
  public void method(final int arg1, int arg2){
    final int val1 = 0;
    int val2 = 0;

    field = 10;

    // arg1 = 20;
    // arg2 = 20;
    
    // val1 = 30;
    // val2 = 30;

  
  Calculator calc = new Calculator(){
    @Override
    public int sum(){
      int result = field + arg1 + arg2 + val1 + val2;
      return result;
    }

  };

  System.out.println(calc.sum());
  }
}
