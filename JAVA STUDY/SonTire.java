public class SonTire extends Tire {
  public SonTire(String location, int maxRotation){
    super(location, maxRotation);
  }
  
  @Override
  public boolean roll(){
    ++accumulatedRotation;
    if(accumulatedRotation < maxRotation){
      System.out.println(location + "tire");
      return true;
    }
    else{
      System.out.println("펑크");
      return false;
    }


  }


}
