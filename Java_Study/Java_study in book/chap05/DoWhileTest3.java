import java.util.Scanner;
public class DoWhileTest3 {
	public static void main(String args[]) {
		int choice;
		Scanner stdin = new Scanner(System.in);
		do {
			System.out.println("==== 반복문 종류 설명 ====");
			System.out.println("  1. while 반복문");
			System.out.println("  2. do-while 반복문");
			System.out.println("  3. for 반복문");
			System.out.println("끝내시려면 99를 입력하세요");
			System.out.print("원하는 번호를 입력하세요 : ");
			choice = stdin.nextInt();
			switch(choice)
			{
			case 1 :
				System.out.println("****while 반복문****");
		    	System.out.println("조건을 먼저 검사하고 조건이 참일 경우 반복 부분을 수행하는 반복문");
		    	break;
		    case 2 :
		    	System.out.println("****do-while 반복문****");
		    	System.out.println("반복 부분을 먼저 수행하고 조건을 검사한다. 최소한 한 번은 수행되는 반복문");
		    	break;
		    case 3 :
		    	System.out.println("****for 반복문****");
		    	System.out.println("지정된 횟수만큼 반복 부분을 수행하는 반복문");
		    	break;	
		    case 99 :
		        System.out.println("사용해 주셔서 감사합니다");
                break;		     
		    default :
		    	System.out.println("숫자를 잘못 입력하셨습니다");
		    }
			System.out.println();
		} while( choice != 99 );
	}
}