import java.util.Scanner;
public class WhileTest2 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("원하는 단을 입력하세요 : ");
		int dan = stdin.nextInt();
		int x = 1;
		while (x <= 9)
		{
			System.out.println(dan + " * " + x + " = " + dan * x);
			x++;
		}
	}
}