import java.io.*;
import java.util.Scanner;
class DataInputStreamTest1 {	
	public static void main(String args[]) throws IOException {
		Scanner stdin = new Scanner(System.in);
		System.out.print("입력 파일명을 입력하세요 : ");
		String s = stdin.next();
		FileInputStream fis = new FileInputStream(s);
		DataInputStream dis = new DataInputStream(fis);
		System.out.println(dis.readBoolean());
		System.out.println(dis.readByte());
		System.out.println(dis.readChar());
		System.out.println(dis.readDouble());
		System.out.println(dis.readFloat());
		System.out.println(dis.readInt());
		System.out.println(dis.readLong());
		System.out.println(dis.readShort());
		fis.close();
	}
}