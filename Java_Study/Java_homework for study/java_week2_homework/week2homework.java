package school_4_2_1;
import java.util.Scanner;

class Engine{
	String capacity;
	String fuel;
	private int price =20000000;
	public Engine(int cc,int fuel) {
		if(cc==1) {
			capacity ="2000cc이하";
			price+=0;			
		}
		else
		{
			capacity ="2000cc이상";
			price+=10000000;
		}
		if(fuel==1) {
			this.fuel="가솔린";
			price+=5000000;								
		}
		else
			this.fuel="디젤";
	}
	public int getprice() {
		return price;
	}
}
class Car{
	String color;
	Engine e;
	public Car(String c, int cc, int fuel) {
		color =c;
		e= new Engine(cc,fuel);
	}
	public String getprice() {
		return "당신이 요청한 "+e.capacity+"의"+e.fuel+"차량(컬러:"+color+")의 가격은 : "
				+e.getprice();
	}
}
public class week2homework {
	public static void main(String args[]) {
		String color;
		int cc,fuel;		
		System.out.print("구입하고 싶은 차의 배기량은 (1:2000cc이하 2:2000cc이상) : ");
		Scanner stdin =new Scanner(System.in);
		cc =stdin.nextInt();
		System.out.print("구입하고 싶은 차의 연료는 (1:가솔린 2:디젤) : ");
		stdin =new Scanner(System.in);
		fuel =stdin.nextInt();
		System.out.print("구입하고 차의 컬러는 : ");
		stdin =new Scanner(System.in);
		color =stdin.next();
	    Car c =new Car(color,cc,fuel);
		System.out.println(c.getprice());		
		System.out.println("차량의 가격은 : "+c.e.getprice());
	}

}
