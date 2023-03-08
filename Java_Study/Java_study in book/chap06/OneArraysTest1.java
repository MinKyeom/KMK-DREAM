import java.util.Scanner;
public class OneArraysTest1 {
	public static void main(String args[]) 
	{
		int inum[] = {8,7,3,6,9,6,8,7,0,4,1,2};
		Scanner stdin = new Scanner(System.in);
		System.out.print("찾고 싶은 숫자 입력 : ");
		int key = stdin.nextInt();
		int count = 0;
		for (int i = 0 ; i < inum.length ; i++) 
		{
			if ( inum[i] == key ) {
				count++;
				System.out.println((i+1) + "번째 데이터와 일치");
			}
		}
		if (count == 0)
			System.out.println(key + "값은 배열에 없습니다");
		else
			System.out.println(key+ "값은 배열에 "+count+"개 있습니다");
	}
}
