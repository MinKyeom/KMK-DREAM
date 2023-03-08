public class ArithmeticOPTest2 {
	public static void main(String aa[])
	{
		byte a=127, b = 2;
		byte c =(byte)(a*b);
		System.out.println("a*b의 결과를 byte로 변환 출력 : " + c);
		int d = a * b;
		System.out.println("a*b의 결과를 int로 출력 : " + d);
		int i = 1000000, j = 1000000;
		int k = i * j;
		System.out.println("백만*백만의 결과를 int로 출력 : " + k);
		long m = (long)(i*j);
		System.out.println("곱셈(int 연산)의 결과를 long으로 변환한 후 출력 : " + m);
		m = (long)i*j;
		System.out.println("i를 long 값으로 변환 후 곱셈(long 연산)하여 출력 : " + m);
		m = (long)i*(long)j;
		System.out.println("백만을 long으로 변환 후 곱셈(long 연산) 결과를 출력 : " + m);

		
	}	
}