public class DmbCellPhone extends CellPhone{
  int channel;

  DmbCellPhone(String model, String color, int channel){
    this.model =model; // CellPhone으로부터 상속 받음
    this.color = color; // CellPhone으로부터 상속 받음
    this.channel = channel;
  }
}

