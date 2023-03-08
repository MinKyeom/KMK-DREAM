public class BreakLabelTest2{
	public static void main(String args[]) 
	{
		int i=2,j; 
		Loop : while(true)
		{
			j=1;
			if (i < 10)
				System.out.println("\n=== " + i + "´Ü ===");
			Innerloop : while(true)
			{
				if ( j > 9 ) break;				
				if ( i > 9 ) break Loop;
				System.out.println(i+" * " + j + " = " + i*j);
				j++;
			}	
			System.out.println();
			i++;
		}	
	}
}
