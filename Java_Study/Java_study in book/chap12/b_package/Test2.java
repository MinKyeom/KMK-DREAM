package b_package;
import a_package.Test1;
//¶Ç´Â import a_package.*;
public class Test2 {
	public static void main(String args[]) {
		Test1 ss = new Test1();
		System.out.println(ss.sum(10,20));
	}
}
