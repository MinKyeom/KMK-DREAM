class Engine {
	int capacity;
	int cylinder;
	String fuel;
	public Engine(......) {
		.....
	}
}
class EngineCar {
	......
	Engine e;
	......
	public EngineCar(......) {
		e = new Engine(......);
	}
	......	
}

public class EnginCarTest {
	......
	EngineCar ec = new EngineCar(.....);
	System.out.println(ec.e.capacity);
	System.out.println(ec.e.fuel);
	......
}
