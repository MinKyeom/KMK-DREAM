import java.util.Scanner;
public class ContinueTest1 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("원하는 정수 입력(짝수의 합) : ");
		int num = stdin.nextInt();
		int i, sum=0;
		for (i=1 ; i <= num ; i++) {
			if (i % 2 == 1) continue;
			sum = sum + i;
		}
		System.out.println("1부터 " + num + "까지 짝수의 합 = " + sum);
	}
}