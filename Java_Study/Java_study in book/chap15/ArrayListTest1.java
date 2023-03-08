import java.util.*;
class ArrayListTest1 {
	public static void main(String[] args) {
		String[] name = {"kim","lee","park","jung","oh"};
		ArrayList<String> lname = new ArrayList<String>(Arrays.asList(name));
		System.out.println("초기 값 : "+lname);
		lname.add("ha");
		System.out.println("\"ha\" 추가된 후의 값 : "+lname);
		lname.set(0,"김");
		lname.add(3,"곽");
		System.out.println("\"김\"으로 변경되고 \"곽\"이 추가된 값 : "+lname);
		Collections.shuffle(lname);
		System.out.println("shuffle() 메소드가 적용된 값 : "+lname);
		Collections.sort(lname);
		System.out.println("sort() 메소드가 적용된 값 : "+lname);
		System.out.println("5번째 요소의 값 : "+lname.get(4));
		Collections.fill(lname, "김");
		System.out.println("모든 요소를 \"김\"으로 설정된 값 : "+lname);	
	}
}
