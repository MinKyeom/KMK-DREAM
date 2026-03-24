public class SupersonicAirplaneExample {
  public static void main(String[] args){
    SupersonicAirplane sa = new SupersonicAirplane();
    sa.flyMode = SupersonicAirplane.SUPERSONIC;
    sa.fly();

    sa.flyMode = SupersonicAirplane.NOMAL;
    sa.fly();
  }

  
}
