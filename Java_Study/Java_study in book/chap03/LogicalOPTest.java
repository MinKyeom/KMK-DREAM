public class LogicalOPTest {
	public static void main(String args[]) 
	{
		boolean a;
		a = (20 > 10) || (30 > 40);
		System.out.println("20이 10보다 크거나 또는(논리합 ||) 30이 40보다 큰가? " + a);
		a = (20 > 10) && (30 > 40);
		System.out.println("20이 10보다 크고 그리고(논리곱 &&) 30이 40보다 큰가? " + a);
		a = ! true;
		System.out.println("ture의 !(not)은? " + a);
		System.out.println("20이 10보다 크거나 또는(논리합 ||) 30이 40보다 큰가? " + ((20 > 10) || (30 > 40)));
		System.out.println("20이 10보다 크고 그리고(논리곱 &&) 30이 40보다 큰가? " + ((20 > 10) && (30 > 40)));
		System.out.println("ture의 !(not)은? " + (! true));		
	}
}