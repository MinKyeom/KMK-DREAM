public class WrapperTest1 {
	public static void main(String args[]) {
		int num1 = 20;
		Integer num2 = new Integer(30);
		double div = num1 / num2.doubleValue();
		System.out.println("나눈 값 : " + div);
		System.out.println("두 수가 같은가? : " + num2.equals(num1));
	}
}
