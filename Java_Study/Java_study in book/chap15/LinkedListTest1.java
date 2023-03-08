import java.util.*;
public class LinkedListTest1 {
	public static void main(String[] args) {
		LinkedList box = new LinkedList();
		box.add("전체 박스");
		box.add(new Box1("white",3,3,3));
		box.add(new Box1("red",5,5,5));
		box.add(new Box1("black",7,7,7));
		box.add(2,new Box1("yellow",9,9,9));
		System.out.println(box);
		for(int i = 1 ; i < box.size() ; i++) {
			Box1 b = (Box1)box.get(i);
			System.out.println(b.color + " 박스의 부피는 : " + b.vol);			
		}
		box.remove(3);
		System.out.println(box);
	}
}
class Box1 {
	String color;
	public int vol;
	
	public Box1(String c, int w, int d, int h) {
		color = c;
		vol = w*d*h;
	}
}