import java.util.*;
class HashMapTest1 {	
	public static void main(String[] args) {
		HashMap<String,String> hm = new HashMap<String,String>();
		hm.put("성명","김한국");
		hm.put("나이","21");
		Object x = hm.put("국적","대한민국");
		if (x != null) 
			System.out.println("대체된 값 : " + x);
		else
			System.out.println("맵에 추가");
		System.out.println(hm);
		Object y = hm.put("나이","24");
		if (y != null)
			System.out.println("대체된 값 : "+ x);
		System.out.println(hm);
		Object z = hm.remove("나이");
		if (z != null) 
			System.out.println("삭제된 값 : "+ z);
		else 
			System.out.println("키가 존재하지 않음");
		System.out.println(hm);
	}
}
