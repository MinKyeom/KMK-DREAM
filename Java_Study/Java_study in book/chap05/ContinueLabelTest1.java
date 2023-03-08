public class ContinueLabelTest1 {
	public static void main(String args[]) 
	{
		int i,j; 
		Outer : for (i=2; i<=9 ; i=i+1)
		{
			System.out.println("=== " + i + "´Ü ===");
			for(j=1; j<=9; j=j+1)
			{	
				if (j == 3) continue Outer;
				System.out.println(i+" * " + j + " = " + i*j);
			}	
		}	
	}
}