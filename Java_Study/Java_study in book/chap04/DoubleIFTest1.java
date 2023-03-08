import java.util.Scanner;
public class DoubleIFTest1 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("성적을 입력하세요 : ");
		int grade = stdin.nextInt();
/*		if (grade >= 90)
			System.out.println("A학점 취득 성공");
		else
			System.out.println("A학점 취득 실패"); */	
		System.out.println((grade >= 90) ? "A학점 취득 성공" : "A학점 취득 실패");

		System.out.println("감사합니다");	
	}
}