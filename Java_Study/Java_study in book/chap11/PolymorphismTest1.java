class Am {
	int count=1;
	void callme() {
		System.out.println("Am의 callme() 실행, count 값 : "+count);
	}
}
class Bm extends Am {
	int count=2;
	void callme() {     
		System.out.println("Bm의 callme() 실행, count 값 : "+count);
	}
}

class Cm extends Am {   
	int count=3;
	void callme() {     
		System.out.println("Cm의 callme() 실행, count 값 : "+count);
	}
}

class PolymorphismTest1 {
	public static void main(String args[]) {
		Am r = new Am();
		r.callme();
		System.out.println("r.count 값 : " + r.count);
		r = new Bm();
		r.callme();
		System.out.println("r.count 값 : " + r.count);
	    r = new Cm();
	    r.callme();
	    System.out.println("r.count 값 : " + r.count);
	}
}
