import java.net.*;
public class UDPSender {
  public static void main(String args[]) throws Exception {
    DatagramSocket ds = new DatagramSocket(); 
    InetAddress ia = InetAddress.getByName(args[0]);
    int port = Integer.parseInt(args[1]);
    byte buffer[] = args[2].getBytes();
    DatagramPacket dp = new DatagramPacket(buffer, buffer.length, ia, port); 
    ds.send(dp);
  }
}  