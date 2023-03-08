package school_4_2_1;

import java.util.*;

class week14homework2{
	public static void main(String args[]){
		Scanner p = new Scanner(System.in);
		System.out.print("가위, 바위, 보 게임 선택(1:가위, 2:바위, 3:보) : ");
		int user = p.nextInt()-1;
		Random random = new Random();
		int com = random.nextInt(3);
		HashMap<Integer,String> hm = new HashMap<Integer,String>();
		hm.put(0, "가위");
		hm.put(1, "바위");
		hm.put(2, "보");
		Object value1 = hm.get(user);
		System.out.println("당신은 " + value1 + "를 냈습니다");
		Object value2 = hm.get(com);
		System.out.println("컴퓨터는 " + value2 + "를 냈습니다");
		System.out.println("=================================");
		System.out.print("게임 결과 : ");
		if(user == com)
			System.out.println("비겼습니다");
		else if(user == (com+1) % 3)
			System.out.println("당신이 이겼습니다");
		else
			System.out.println("컴퓨터가 이겼습니다");
	}
}