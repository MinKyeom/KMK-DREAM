import java.util.*;
class HashSetTest1 {
	public static void main(String[] args) {
		HashSet<Integer> odd = new HashSet<Integer>();
		HashSet<Integer> even = new HashSet<Integer>();
		for(int i=1 ; i <= 5 ; i=i+2 ){
			odd.add(i);
			even.add(i+1);
		}
		boolean setChanged = odd.add(5);
		System.out.println("odd에 5 추가 성공? : " + setChanged);
		setChanged = even.add(12);
		System.out.println("even 12 추가 성공? : " + setChanged);
		System.out.println("odd 집합 : " + odd);
		System.out.println("even 집합 : "+ even);
		System.out.println("odd에서 가장 작은 값은 : "+Collections.min(odd));
		System.out.println("even에서 가장 큰 값은 : "+Collections.max(even));
		Iterator<Integer> it = even.iterator();
		int sum=0;
		while(it.hasNext()){
			sum = sum + it.next();
		}
		System.out.println("even 집합의 합은 : "+sum);
	}
}
