public class MultiArraysTest3 {
	public static void main(String args[]) 
	{
		int[][][] threeD = new int[3][4][5];
		int i, j, k, count=11;
		for( i=0 ; i < threeD.length ; i++)
			for( j=0; j < threeD[i].length ; j++)
				for( k=0; k < threeD[i][j].length ; k++)
				{	
					threeD[i][j][k] = count;
					count++;
				}
		for(i=0; i<threeD.length; i++) 
		{
			System.out.println((i+1) + "번째 2 차원 배열 ");
			for(j=0; j<threeD[i].length; j++) 
			{
				for(int val : threeD[i][j])
					System.out.print(val + " ");
				System.out.println();
			}	
			System.out.println();
		}
	}
}

