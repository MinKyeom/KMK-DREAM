import java.util.*;

class LinkedListTest2 {
	public static void main(String[] args) {
		ArrayList<Integer> alist = new ArrayList<Integer>();
		LinkedList<Integer> llist = new LinkedList<Integer>();
		long start, stop;
		
		start = System.currentTimeMillis();
		for (int i=0 ; i<=100000000 ; i++) 
			alist.add(i);
		stop = System.currentTimeMillis();
		System.out.println("ArrayList - ¼øÂ÷Àû »ðÀÔ : " + (stop-start));
		
		start = System.currentTimeMillis();
		for (int i=0 ; i<=100000000 ; i++)
			llist.add(i);
		stop = System.currentTimeMillis();
		System.out.println("LinkedList - ¼øÂ÷Àû »ðÀÔ : " + (stop-start));
		
		start = System.currentTimeMillis();
		for (int i=0 ; i < 1000 ; i++)
			alist.add(500,i);
		stop = System.currentTimeMillis();
		System.out.println("ArrayList - Áß°£ »ðÀÔ : " + (stop-start));
		
		start = System.currentTimeMillis();
		for (int i=0 ; i < 1000 ; i++)
			llist.add(500,i);
		stop = System.currentTimeMillis();
		System.out.println("LinkedList - Áß°£ »ðÀÔ : " + (stop-start));
	}
}
