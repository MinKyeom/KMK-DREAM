import java.util.Scanner;
public class ForTest3 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("두 개의 숫자를 입력하세요(공백으로 구분) : ");
		int m = stdin.nextInt();
		int n = stdin.nextInt();
		int i;
		for( i=1; i<=m*n ; i++ )
		{
			if((i%n == 0) && (i%m == 0))
				break;
		}
		System.out.print("최소 공배수는 " + i + "입니다. ");
		for( i=n; i>=1 ; i-- )
		{
			if((m%i == 0) && (n%i == 0))
				break;
		}
		if(i==1)
			System.out.print("최대 공약수가 없습니다.");
		else
			System.out.print("최대 공약수는 " + i + "입니다. ");
	}
}
