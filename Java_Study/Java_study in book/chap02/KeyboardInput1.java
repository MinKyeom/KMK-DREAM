import java.util.Scanner;
public class KeyboardInput1 {
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("몇 번째 프로그램인지 입력하세요 : ");
		String s = stdIn.next();
		System.out.println(s + " 번째로 작성해 보는 자바 프로그램입니다 ");
	}
}
