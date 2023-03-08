class Box6 {
	int width;
	int height;
	int depth;
	double dwidth;
	double dheight;
	double ddepth;
	public Box6(int w, int h, int d)
	{
		width = w;
		height = h;
		depth = d;
	}
	public Box6(double w, double h, double d)
	{
		dwidth = w;
		dheight = h;
		ddepth = d;
	}
}
public class Box6Test1 {
	public static void main(String args[]) {
		Box6 mybox1 = new Box6(10,20,30);
		int vol = mybox1.width * mybox1.height * mybox1.depth;
		System.out.println("박스의 부피(정수 매개 변수) : " + vol);
		mybox1 = new Box6(10.5, 20.5, 30.5);
		double dvol = mybox1.dwidth * mybox1.dheight * mybox1.ddepth;
		System.out.println("박스의 부피(실수 매개 변수) : " + dvol);
		mybox1 = new Box6(10,20,30.5);
		dvol = mybox1.dwidth * mybox1.dheight * mybox1.ddepth;
		System.out.println("박스의 부피(정수와 실수 혼합) : " + dvol);
	}
}