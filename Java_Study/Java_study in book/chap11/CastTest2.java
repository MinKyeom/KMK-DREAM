class Rectangle5 {
	public int width;
	public int height;
	public Rectangle5(int w, int h) {
		width = w;
		height = h;		
	}
	public int computeRectangleArea() {
		return width * height;
	}
}
class Cube5 extends Rectangle5 {
	public int depth;
	public Cube5(int w, int h, int d) {
		super(w,h);
		depth = d;
	}
	public int computeCubeArea() {
		return super.computeRectangleArea() * depth;
	}
}
public class CastTest2 {
	public static void main(String args[]) {
		Rectangle5 r = new Cube5(10,20,30);
		System.out.println("정사각형의 넓이는 : "+r.computeRectangleArea());
		//System.out.println("넓이는 : "+r.computeCubeArea());
		Cube5 c = (Cube5) r;
		System.out.println("직육면체의 부피는 : "+c.computeCubeArea());
	}
}
