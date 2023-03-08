public class TestDouble {
	public static void main(String[] args) {
		double r = 5.0;
		double pi = 3.14159;

		System.out.printf("반지름이 %f인 원의 넓이는 %f입니다\n", 5.0, 3.14159*5*5);
		System.out.printf("반지름이 %f인 원의 넓이는 %f입니다\n", r, pi*r*r);
		System.out.printf("반지름이 %e인 원의 넓이는 %e입니다\n", r, pi*r*r);
		System.out.printf("123.456을 %%f로 : %f\n", 123.456);
		System.out.printf("123.456을 %%e로 : %e\n", 123.456);
		System.out.printf("-123.456을 %%E로 : %E\n", -123.456);
	}
}
