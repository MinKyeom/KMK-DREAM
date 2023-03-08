import java.util.Scanner;

public class TernaryOPTest {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("한 개의 숫자를 입력 : ");
		int a = stdin.nextInt();
		boolean flag;
		flag = (a % 2 == 0) ? true : false;
		System.out.print(a +"이(가)  짝수입니까? : ");
		System.out.println(flag);
	}
}