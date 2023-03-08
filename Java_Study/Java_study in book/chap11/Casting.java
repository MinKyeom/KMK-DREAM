class Car {
}
class Bus extends Car{
}
public class Casting {
	public static void main(String args[]){
		Car c1;
		Bus b1 = new Bus();
		c1 = b1; // c = (Car)b;
		Car c2 = new Car();
		//Bus b2 = (Bus)c2;
		Car c3 = new Bus();
		Bus b3 = (Bus)c3;
		if(c3 instanceof Bus)
			System.out.println("dfsdf");
	}

}
