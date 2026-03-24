public class SupersonicAirplane extends Airplane {
  public static final int NOMAL = 1;
  public static final int SUPERSONIC = 2;

  public int flyMode = NOMAL;

  @Override
  public void fly(){
    if(flyMode == SUPERSONIC){
      System.out.println("초음속");
    }
    else{
      super.fly();
    }
  }
  
}
