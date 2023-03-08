public class DoWhileTest1 {
	public static void main(String args[]) 
	{
		int hap=0, count=1;
		do
		{
			hap = hap + count;
			count = count + 1;
		} while (count <= 10);
		System.out.println("1부터 10까지의 합은 "+ hap + " 입니다");
	}
}