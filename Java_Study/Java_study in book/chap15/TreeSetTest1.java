import java.util.*;
class TreeSetTest1 {
	public static void main(String[] args) {
		TreeSet<Integer> low = new TreeSet<Integer>();
		TreeSet<Integer> even = new TreeSet<Integer>();
		
		//LinkedList<Integer> low = new LinkedList<Integer>();
		//LinkedList<Integer> even = new LinkedList<Integer>();
		
		for (int i=4 ; i>=0 ; i-- )	{
			low.add(i);
			even.add(i*2);
		}
		System.out.println("low집합 : "+low+" even집합 : "+even);
		TreeSet<Integer> union = new TreeSet<Integer>(low);
		//LinkedList union = new LinkedList(low);
		TreeSet<Integer> intersection = new TreeSet<Integer>(low);
		TreeSet<Integer> difference = new TreeSet<Integer>(low); 
		
		union.addAll(even);
		intersection.retainAll(even);
		difference.removeAll(even);
		
		System.out.println("low와 even의 합집합 : " + union);
		System.out.println("low와 even의 교집합 : " + intersection);
		System.out.println("low와 even의 차집합 : " + difference);
	}
}