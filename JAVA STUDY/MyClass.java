public class MyClass {
  RemoteControl rc = new Television();

  // 생성자
  MyClass(){
  }

  MyClass(RemoteControl rc){
    this.rc = rc;
    rc.turnOn();
    rc.setVolume(5);
  }

  //메소드
  void methodA(){

    RemoteControl rc  = new SmartTelevision();
    rc.turnOn();
    rc.setVolume(10);
  } 
}
