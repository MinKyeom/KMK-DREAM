import java.util.Scanner;
class Ramyon1 {
	String ramyon="라면";
	String water="물";
	String onion="파";
	void boilwater() {
		System.out.println(water+"을 끓인다");
	}
	void cooking() {
		System.out.println(ramyon+"과 "+onion+"를 넣고 끓여 요리완성. 맛있게 드세요!!!");		
	}
}

class RiceRamyon1 {
	Ramyon1 rm = new Ramyon1();
	String rice="떡";
	void topping() {
		System.out.println(rice+"을 넣는다");			
	}
}	

class CheeseRamyon1 {
	Ramyon1 rm = new Ramyon1();
	String cheese = "치즈";
	void topping() {
		System.out.println(cheese+"를 넣는다");		
	}
}

public class CompositeRamyonTest {
	public static void main(String args[]) {
		int s;
		do {
			System.out.print("만들고 싶은 요리를 입력하세요(1:일반라면,2:떡라면,3:치즈라면,99:종료) : ");
			Scanner stdin = new Scanner(System.in);
			s = stdin.nextInt();
			if (s == 1) {
				Ramyon1 r = new Ramyon1();
				r.boilwater();
				r.cooking();
			} else if (s == 2) {
				RiceRamyon1 rr = new RiceRamyon1();
				rr.rm.boilwater();
				rr.topping();
				rr.rm.cooking();
			} else if (s == 3) {
				CheeseRamyon1 cr = new CheeseRamyon1();
				cr.rm.boilwater();
				cr.topping();
				cr.rm.cooking();
			}
		} while ( s != 99);
		System.out.print("감사합니다");	
	}
}

