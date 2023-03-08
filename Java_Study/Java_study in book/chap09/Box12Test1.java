class Box12 {
	private int ivol;
	public Box12(int w, int h, int d)
	{
		ivol = w * h * d;
	}
	public String get_ivol() {
		return "박스의 부피는 " + ivol;
	}
}

public class Box12Test1 {
	public static void main(String args[]) {
		Box12 mybox[] = new Box12[10];
		for(int i = 0 ; i < mybox.length ; i++) {
			mybox[i] = new Box12(i*10, i*20, i*30);
		}
		for(Box12 mb : mybox) {
			System.out.println(mb.get_ivol());
		}

	}
}
