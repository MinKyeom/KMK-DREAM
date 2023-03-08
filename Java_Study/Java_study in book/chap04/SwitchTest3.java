public class SwitchTest3 {
	public static void main(String args[]) 
	{
		char c = 'A';
		//char c = 'a';
		switch (c)
		{
			case 'A':
			case 'B':
				System.out.print("우수한 성적입니다");
				break;
			case 'C':
			case 'D':
				System.out.print("분발하십시요");
				break;
			case 'F':
				System.out.print("많은 노력이 필요합니다");
				break;
			default:
				System.out.print("정확한 성적이 아닙니다");
		}
	}
}