package school_4_2_1;


class Box2<T> {
	T vol;
	void setVolume(T v){
		vol=v;
	}
	T getVolume(){
		return vol;
	}
}

public class week7homework3 {
	public static void main(String args[]) {
		Box2<Integer> ibox = new Box2<Integer>();
		ibox.setVolume(200);
		//ibox.setVolume(32.3);
		System.out.println("<Integer>박스의 부피는 : " + ibox.getVolume());
		Box2<Double> dbox = new Box2<Double>();
		dbox.setVolume(123.456);
		//dbox.setVolume(300);
		System.out.println("<Double>박스의 부피는 : " + dbox.getVolume());
	}
}

