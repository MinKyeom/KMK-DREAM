public class SmartTelevision implements RemoteControl,Searchable {

  public void turnOn() {
    System.out.println("On");
  }

  public void turnOff() {
    System.out.println("Off");
  }

  public void setVolume(int volume) {
    System.out.println("volume");
  }

  public void search(String url) {
    System.out.println("Search");
  }
  
}
