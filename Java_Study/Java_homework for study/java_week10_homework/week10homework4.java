package school_4_2_1;

import java.util.*;

public class week10homework4 {
	public static void main(String[] args) {
		TreeSet<Integer> low = new TreeSet<Integer>();
		TreeSet<Integer> even = new TreeSet<Integer>();
		

		for (int i=4 ; i>=0 ; i-- )	{
			low.add(i);
			even.add(i*2);
		}
		System.out.println("low���� : "+low+" even���� : "+even);
		TreeSet<Integer> union = new TreeSet<Integer>(low);
		//LinkedList union = new LinkedList(low);
		TreeSet<Integer> intersection = new TreeSet<Integer>(low);
		TreeSet<Integer> difference = new TreeSet<Integer>(low); 
		
		union.addAll(even);
		intersection.retainAll(even);
		difference.removeAll(even);
		
		System.out.println("low�� even�� ������ : " + union);
		System.out.println("low�� even�� ������ : " + intersection);
		System.out.println("low�� even�� ������ : " + difference);
	}
}
