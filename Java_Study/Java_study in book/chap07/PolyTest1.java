abstract class Figure1 {
	abstract void draw();
}
class Triangle1 extends Figure1 {
	public void draw() {
		System.out.println("다형성 : 삼각형을 그린다");
	}
}
class Rectangle1 extends Figure1 {
	public void draw() {
		System.out.println("다형성 : 사각형을 그린다");
	}
}
class Oval1 extends Figure1 {
	public void draw() {
		System.out.println("다형성 : 타원형을 그린다");
	}
}
class Polydraw {
	public void pdraw(Figure1 f) {
		f.draw();
	}
	/*
	public void pdraw(Triangle1 f) {
		f.draw();
	}
	public void pdraw(Rectangle1 f) {
		f.draw();
	}
	public void pdraw(Oval1 f) {
		f.draw();
	}
	*/
}
public class PolyTest1 {
	public static void main(String args[]) {
		Polydraw p = new Polydraw();
		Figure1 fg1 = new Triangle1();
		Figure1 fg2 = new Rectangle1();
		Figure1 fg3 = new Oval1();
		/*
		Triangle1 fg1 = new Triangle1();
		Rectangle1 fg2 = new Rectangle1();
		Oval1 fg3 = new Oval1();
		*/		
		p.pdraw(fg1);
		p.pdraw(fg2);
		p.pdraw(fg3);
	}
}	