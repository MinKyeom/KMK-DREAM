import java.util.*;

class LinkedHashMapTest1 {
	public static void main(String args[]) {
		LinkedHashMap<String,Integer> lm = new LinkedHashMap<String,Integer>();
		lm.put("국어", 98);
		lm.put("영어", 100);
		lm.put("수학", 86);
		lm.put("사회", 99);
		lm.put("과학", 89);
		System.out.println("당신의 성적 : " + lm + total_avg(lm));
	}
	
	public static String total_avg(Map m) {
		int total = 0;
		int count = m.size();
		Collection<Integer> c = m.values();
		Iterator<Integer> iterator = c.iterator();		
		while(iterator.hasNext()) {
			total = total + iterator.next();
		}
		return "  총점=" + total + " 평균=" + (double)total/count;
	}
}