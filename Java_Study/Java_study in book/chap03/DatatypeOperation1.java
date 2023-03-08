import java.util.Scanner;
public class DatatypeOperation1 {
	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);
		System.out.print("첫 번째 정수를 입력 : ");
		int first = stdin.nextInt();
		System.out.print("두 번째 정수를 입력 : ");
		int  second = stdin.nextInt();
		double avg1 = (first+second) / 2 ;
		System.out.println("정수 연산 : 평균은("+first+"+"+second+")/2 = "+avg1+" 입니다");
		double avg2 = (first+second) / 2.0 ;
		System.out.println("실수 연산 : 평균은("+first+"+"+second+")/2.0 = "+avg2+" 입니다");
	}
}
