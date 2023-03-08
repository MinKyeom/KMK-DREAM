class Rectangle4 {
	public int width;
	public int height;
	public Rectangle4(int w, int h) {
		width = w;
		height = h;		
	}
	public int computeRectangleArea() {
		return width * height;
	}
}
class Cube4 extends Rectangle4 {
	public int depth;
	public Cube4(int w, int h, int d) {
		super(w,h);
		depth = d;
	}
	public int computeCubeArea() {
		return super.computeRectangleArea() * depth;
	}
}
public class CastTest1 {
	public static void main(String args[]) {
		Rectangle4 r = new Cube4(10,20,30);
		System.out.println("³ĞÀÌ´Â : "+r.computeRectangleArea());
		//System.out.println("³ĞÀÌ´Â : "+r.computeCubeArea());
		//Cube4 c = new Rectangle4(10,20);
	}
}
