import java.util.*;

class StackTest1 {
	public static void main(String args[]) {
		Stack<String> stack = new Stack<String>();
		System.out.println("스택에 push : " + stack.push("경기도"));
		System.out.println("스택에 push : " + stack.push("충청도"));
		System.out.println("스택에 push : " + stack.push("강원도"));
		System.out.println("스택에 push : " + stack.push("전라도"));
		System.out.println("스택에 push : " + stack.push("경상도"));
		System.out.println("스택에 push : " + stack.push("제주도"));
		System.out.println("=============================");
		int n = stack.search("제주도");
		if (n != -1)
			System.out.println("스택에서 숫자 \"제주도\"의 위치는 : "+n+"번째 입니다");
		else
			System.out.println("스택에서 숫자 \"제주도\"가 없습니다");
		System.out.println("=============================");
		while(!stack.empty()) {
			Object obj = stack.pop();
			System.out.println("스택에서 pop : " + obj);
		}
	}
}

