import java.net.*;
public class UDPReceiver {
  public static void main(String args[]) throws Exception {
    int port = Integer.parseInt(args[0]);
    int times = Integer.parseInt(args[1]);
    DatagramSocket ds = new DatagramSocket(port); 
    int i=1 ; 
    while( i <= times) {    
      byte buffer[] = new byte[30]; 
      DatagramPacket dp = new DatagramPacket(buffer, buffer.length);
      ds.receive(dp); 
      String str = new String(dp.getData());
      System.out.println("수신된 데이터 : " + str);
      ++i;
    }
  } 
}