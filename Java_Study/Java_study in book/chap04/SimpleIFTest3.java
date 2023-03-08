import java.util.Scanner;
public class SimpleIFTest3 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("성적을 입력하세요 : ");
		int grade = stdin.nextInt();
		if (grade >= 90)
		{
			System.out.println("축하합니다 ");
			System.out.println("A학점을 취득하셨습니다 ");
		}	
		System.out.println("감사합니다");
	}
}