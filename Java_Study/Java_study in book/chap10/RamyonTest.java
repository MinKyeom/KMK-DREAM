import java.util.Scanner;
class Ramyon {
	String ramyon="���";
	String water="��";
	String onion="��";
	void boilwater() {
		System.out.println(water+"�� ���δ�");
	}
	void cooking() {
		System.out.println(ramyon+"�� "+onion+"�� �ְ� ���� �丮�ϼ�. ���ְ� �弼��!!!");		
	}
}

class RiceRamyon extends Ramyon {
	String rice="��";
	void topping() {
		System.out.println(rice+"�� �ִ´�");			
	}
}	

class CheeseRamyon extends Ramyon {
	String cheese = "ġ��";
	void topping() {
		System.out.println(cheese+"�� �ִ´�");		
	}
}

public class RamyonTest {
	public static void main(String args[]) {
		int s;
		do {
			System.out.print("����� ���� �丮�� �Է��ϼ���(1:�Ϲݶ��,2:�����,3:ġ����,99:����) : ");
			Scanner stdin = new Scanner(System.in);
			s = stdin.nextInt();
			if (s == 1) {
				Ramyon r = new Ramyon();
				r.boilwater();
				r.cooking();
			} else if (s == 2) {
				RiceRamyon rr = new RiceRamyon();
				rr.boilwater();
				rr.topping();
				rr.cooking();
			} else if (s == 3) {
				CheeseRamyon cr = new CheeseRamyon();
				cr.boilwater();
				cr.topping();
				cr.cooking();
			}
		} while ( s != 99);
		System.out.print("�����մϴ�");	
	}
}
