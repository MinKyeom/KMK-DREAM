import java.io.*;
import java.util.Scanner;
class FileReaderTest1 {
	public static void main(String args[]) throws Exception {
		Scanner stdin = new Scanner(System.in);
		System.out.print("읽어 들일 파일명을 입력하세요 : ");
		String s = stdin.next();
		FileReader fr = new FileReader(s);
		int i;
		while((i = fr.read()) != -1 ) {
			System.out.print((char)i);
		}
		fr.close();
	}
}