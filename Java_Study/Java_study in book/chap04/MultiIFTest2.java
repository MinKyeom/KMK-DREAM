import java.util.Scanner;
public class MultiIFTest2 {
	public static void main(String args[])
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("숫자를 입력 : ");
		int count = stdin.nextInt();
		if (count < 0 )
		{
			System.out.print("입력된 수 " + count);
			System.out.println("은(는) 음수입니다");
		}
		else if (count == 0)
			System.out.print("입력된 수는 0 입니다");
		else
		{
			System.out.print("입력된 수 " + count);
			System.out.println("은(는) 양수입니다");
		}
	}
}