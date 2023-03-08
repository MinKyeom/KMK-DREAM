public class BreakLabelTest1 {
	public static void main(String args[]) 
	{
		boolean t = true;
		First:{
			Second:{
				Third:{
					System.out.println("Third 블록 'break' 문장 전");	
					if(t) break Second;
					System.out.println("Third 블록 'break' 문장 후");
				}
				System.out.println("Second 블록 문장");
			}
			System.out.println("First 블록 문장");
		}
	    System.out.println("main 블록 문장");
	}	
}