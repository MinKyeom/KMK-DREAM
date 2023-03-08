package school_4_2_1;

import java.util.*;

class week12homework1 {
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		System.out.print("원하는 년과 월을 입력(년월을 공백으로 구분하여 입력) : ");
		int year = s.nextInt();
		int month = s.nextInt();
		GregorianCalendar cal = new GregorianCalendar(year,month-1,1);
		int maxd = cal.getActualMaximum(Calendar.DATE);
		int sday = cal.get(Calendar.DAY_OF_WEEK);
		System.out.println("\n Sun  Mon  Tue  Wed  Thu  Fri  Sat");
		for(int i = 1 ; i < sday ; i ++)
			System.out.print("     ");
		for(int i = 1 ; i <= maxd ; i++){
			if(i > 0 && i < 10)
				System.out.print("  "+i+"  ");
			else
				System.out.print(" "+i+"  ");
		
			if(sday % 7 == 0)
				System.out.println();
			sday++;
		}
	}
}
