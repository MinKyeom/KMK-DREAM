import java.io.*;
public class IOExceptionError {
	public static void main(String args[]) {
		FileReader file = new FileReader("a.txt");
		int i;
		while((i = file.read()) != -1) {
			System.out.print((char)i);
		}
		file.close();
	}
}


