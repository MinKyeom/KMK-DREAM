import java.util.Scanner;
public class ArraysTest1 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		int i;
		double sum=0.0, avg;;
		double dnum[] = new double[5];
		System.out.println("dnum 배열의 길이 : " + dnum.length);
		System.out.print("초기화 하지 않은 dnum[]의 값: ");
		for (i=0; i < dnum.length ; i++)
			System.out.print(dnum[i]+" ");
		System.out.println();
		
		for (i=0; i < dnum.length ; i++){
			System.out.print("dnum["+(i)+"] 번째 데이터 입력 : ");
			dnum[i] = stdin.nextDouble();
		}	
		for (i=0; i < dnum.length ; i++)
			sum = sum + dnum[i];
		System.out.println("배열의 합은 " + sum + "입니다");
		avg = sum/dnum.length; 
		System.out.println("배열 값의 평균은  " + avg + "입니다");
			
	}
}