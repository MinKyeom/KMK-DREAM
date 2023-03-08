import java.util.Scanner;
public class SumofEven {
	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);
		System.out.print("짝수 덧셈을 수행할 두 개의 숫자를 입력(작은 수부터 공간으로 구분) : ");
		int n = stdin.nextInt();
		int m = stdin.nextInt();
		Sum s = new Sum();
		System.out.println(n + "부터 " + m + "까지의 짝수의 합 : " + s.evensum(n, m));
	}
}
