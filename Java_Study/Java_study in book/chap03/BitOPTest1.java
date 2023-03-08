public class BitOPTest1 {
	public static void main(String args[]) 
	{
		int a = 14;
		int b = 11;
		System.out.println("  a = " +a+"("+Integer.toBinaryString(a)+")");
		System.out.println("  b = " +b+"("+Integer.toBinaryString(b)+")");
		System.out.println("a&b = " +(a&b)+"("+Integer.toBinaryString(a&b)+")");
		System.out.println("a|b = " +(a|b)+"("+Integer.toBinaryString(a|b)+")");
		System.out.println("a^b = " +(a^b)+"("+Integer.toBinaryString(a^b)+")");
		System.out.println(" ~b = " +(~b)+"("+Integer.toBinaryString(~b)+")");
	}
}