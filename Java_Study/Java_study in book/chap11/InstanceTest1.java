class Rectangle {
	public int width;
	public int height;
	public Rectangle(int w, int h) {
		width = w;
		height = h;		
	}
	public int computeRectangleArea() {
		return width * height;
	}
}
class Cube extends Rectangle {
	public int depth;
	public Cube(int w, int h, int d) {
		super(w,h);
		depth = d;
	}
	public int computeCubeArea() {
		return super.computeRectangleArea() * depth;
	}
}
public class InstanceTest1 {
	public static void main(String args[]) {
		Rectangle r = new Rectangle(10,20);
		Cube c = new Cube(10,20,30);
		System.out.println("r이 Rectangle의 객체? : "+ (r instanceof Rectangle));
		System.out.println("r이 Cube의 객체? : "+ (r instanceof Cube));
		System.out.println("c가 Rectangle의 객체? : "+ (c instanceof Rectangle));
		System.out.println("c가 Cube의 객체? : "+ (c instanceof Cube));
		System.out.println("=========형 변환 이후===========");
		r = new Cube(20,30,40);
		System.out.println("형 변환 r이 Rectangle의 객체? : "+ (r instanceof Rectangle));
		System.out.println("형 변환 r이 Cube의 객체? : "+ (r instanceof Cube));
		System.out.println("형 변환 r이 Rectangle의 객체? : "+ (c instanceof Rectangle));
		System.out.println("형 변환 r이 Cube의 객체? : "+ (c instanceof Cube));
		System.out.println("=============================");
		System.out.println("r이 Object의 객체? : "+ (c instanceof Cube));
	}
}
