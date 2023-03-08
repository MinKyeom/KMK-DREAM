import java.util.Random;
interface IStack {
	public void push(int item); 
	public int pop();
}	
class FixedStack implements IStack {
	private int stack[];
	private int tos;
	FixedStack(int size) {
		stack = new int[size];
		tos = -1;
	}
	public void push(int item) {  
		if(tos==stack.length-1)  
			System.out.println("스택이 꽉 찼음");
		else 
			stack[++tos] = item;
	}
	public int pop() {  
		if(tos < 0) {
			System.out.println("스택이 비었음");
			return 0;
		}
		else 
			return stack[tos--];
	}
}
public class InterfaceTest1 {
  public static void main(String args[]) {
	  Random r = new Random();
	  FixedStack mystack1 = new FixedStack(10);
	  for(int i=0 ; i<10 ; i++) 
		  mystack1.push(r.nextInt(10));
	  System.out.println("스택 : mystack1");
	  for(int i=0 ; i<10 ; i++) 
		  System.out.print(mystack1.pop() + "  ");	
  }
}
