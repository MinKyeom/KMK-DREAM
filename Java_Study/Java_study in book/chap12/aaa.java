
public class aaa {
	public static void main(String args[]) {
		String name1 = "cskim";
		String name2 = "gentleman";
		name1 = name1 + name2;
		System.out.println(name1);
		String name3 = new String("cskim");
		String name4 = new String("cskim");
		System.out.println(name1 == name2);
		System.out.println(name1 == name3);
		System.out.println(name3 == name4);
		System.out.println(name3.equals(name4));
		/*name3 = name1 + name2;
		name4 = name1 + name2;
		System.out.println(name3 == name4);
		System.out.println(name3);
		System.out.println(name4);*/
		String name11 = "name3 + name4";
		String name12 = "name3 + name4";
		System.out.println("dfsdf==="+(name11 == name12));
		System.out.println(name1);
		System.out.println(name2);
	
	}

}
