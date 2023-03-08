public class AssignOPTest1 {
	public static void main(String args[]) 
	{
		int a = 10;
		System.out.println("a = " + a);
		a += 4;
		System.out.println("a += 4의 결과 " + a);
		a %= 4;
		System.out.println("a %= 4의 결과 " + a);
		a <<= 4;
		System.out.println("a <<= 4의 결과 " + a);
		boolean b = false;
		b &= a > 2;
		System.out.println("b &= a > 2의 결과 " + b);
		b |= a > 2;
		System.out.println("b |= a > 2의 결과 " + b);
	}
}