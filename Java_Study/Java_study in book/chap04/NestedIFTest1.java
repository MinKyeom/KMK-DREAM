import java.util.Scanner;
public class NestedIFTest1 {
	public static void main(String args[])
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("성적을 입력하세요 : ");
		int score = stdin.nextInt();
		if (score >= 80)
		{
			System.out.println("우수 학점군에 속합니다");
			if (score >= 90)	
				System.out.println("A 학점입니다");
			else 
				System.out.println("B 학점입니다");
		}
		else
		{
			if (score >= 60)
			{   
				System.out.println("보통학점군에 속합니다");
				if (score >= 70)	
					System.out.println("C 학점입니다");
				else 
					System.out.println("D 학점입니다");
			}	
			else
				System.out.println("학점취득 실패");
		}
	}	
}