class Box8 {
	int width;
	int height;
	int depth;
	public Box8(int width, int height, int depth)
	{
		this.width = width;
		this.height = height;
		this.depth = depth;
	}
	int volume()
	{
		int vol = width * height * depth;
		return vol;
	}
}
public class Box8Test1 {
	public static void main(String args[]) {
		Box8 mybox1 = new Box8(10,20,30);
		//mybox1.width = 20;
		int vol1 = mybox1.volume();
		System.out.println("정수 박스의 부피 : " + vol1);
	}
}