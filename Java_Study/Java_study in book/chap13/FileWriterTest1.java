import java.io.*;
import java.util.Scanner;
public class FileWriterTest1 {
	public static void main(String args[]) throws Exception {
		Scanner stdin = new Scanner(System.in);
		String source = "비어 있어야 비로소 가득해지는 사랑\n" + " 영원히 사랑한다는 것은\n" + " 평온한 마음으로 아침을 맞는다는 것입니다.\n";
		char input[] = new char[source.length()];
		source.getChars(0, source.length(), input, 0);
		System.out.print("파일명을 입력하세요 : ");
		String s = stdin.next();
		FileWriter fw = new FileWriter(s);
		fw.write(input);
		fw.close();
		System.out.print(s + "파일이 생성되었습니다");
	}
}