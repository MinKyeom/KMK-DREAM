import java.io.*;
import java.net.*;
class ServerSide {
  public static void main(String args[]) throws Exception {
    int port = Integer.parseInt(args[0]);
    int times = Integer.parseInt(args[1]);
    ServerSocket ss = new ServerSocket(port);
    int i = 1;
    while( i <= times) {   
      Socket s = ss.accept();
      OutputStream os = s.getOutputStream();
      DataOutputStream dos = new DataOutputStream(os);
      for(int j = 1 ; j <= 10 ; j++) 	
        dos.writeInt(j);
      s.close();
      ++i;
      }
  } 
}