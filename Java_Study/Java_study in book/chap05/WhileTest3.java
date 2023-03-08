import java.util.Scanner;
public class WhileTest3 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("원하는 팩토리얼 값을 입력 : ");
		int fac = stdin.nextInt();
		int facValue = fac;
		while (fac > 1)
		{
			System.out.print(fac +"*");
			facValue *= --fac;
		}
		System.out.println("1="+ facValue);
	}
}