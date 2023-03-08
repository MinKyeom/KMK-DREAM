import java.io.*;
public class ObjectReadTest1 {
	public static void main(String args[]) throws Exception {
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream("tmp.txt"));
		Object s2 = ois.readObject(); 
		Box mybox2 = (Box)ois.readObject();
		System.out.println(s2);
		System.out.println("박스의 가로는 : "+mybox2.width);
		System.out.println("박스의 세로는 : "+mybox2.height);
		System.out.println("박스의 높이는 : "+mybox2.depth);
		System.out.println("Double 값은 : " + ois.readDouble());
	}
}