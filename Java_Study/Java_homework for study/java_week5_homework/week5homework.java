package school_4_2_1;

import java.util.Scanner;
import java.util.Random;



public class week5homework {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random r=new Random();
		Scanner s =new Scanner(System.in);
		
		while(true)
		{
			System.out.print(">>");
			String str=s.nextLine();
			StringBuffer sb=new StringBuffer(str);
			if(sb.toString().equals("exit"))
			{
				System.out.println("종료합니다...");
				break;
			}
			int index=r.nextInt(str.length());
			while(true)
			{
			int i=r.nextInt(26);
			char c=(char)('a'+i);
			if(sb.charAt(index)!=c)
			{
				sb.replace(index, index+1,Character.toString(c));
				break;
			}
			
		}
		System.out.println(sb);
		
	}
	


}
}