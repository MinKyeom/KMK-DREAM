class OIaa {
	public void show(String str) {
		System.out.println("상위 클래스의 메소드 수행 : " + str);
	}
}
class OIbb extends OIaa {
	public void show(String s) {
		System.out.println("하위 클래스의 메소드 show() 수행 : " + s);
	}
}
public class OverridingTest2 {
	public static void main(String args[]) {
		OIbb oibb = new OIbb();
		oibb.show("쉽다 자바프로그래밍!!!"); 
	}
}