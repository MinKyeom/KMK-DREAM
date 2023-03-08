abstract class Figure {
	abstract void draw();
}
class Triangle extends Figure {
	public void draw() {
		System.out.println("삼각형을 그린다");
	}
}
class Rectangle extends Figure {
	public void draw() {
		System.out.println("사각형을 그린다");
	}
}
class Oval extends Figure {
	public void draw() {
		System.out.println("타원형을 그린다");
	}
}
public class AbstractTest1 {
	public static void main(String args[]) {
		Figure fg1 = new Triangle();
		Figure fg2 = new Rectangle();
		Figure fg3 = new Oval();
		fg1.draw();
		fg2.draw();
		fg3.draw();		
	}
}	