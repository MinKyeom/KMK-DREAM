import java.util.Calendar;
import java.util.Date;

class CalendarExam {
	public static void main(String args[]) {
		Calendar calendar = Calendar.getInstance();
		System.out.print("날짜 : ");
		System.out.print(calendar.get(Calendar.YEAR) + "년 ");
		System.out.print(calendar.get(Calendar.MONTH)+1+"월 ");
		System.out.print(calendar.get(Calendar.DATE) + "일 ");
		System.out.print(calendar.get(Calendar.HOUR) + "시 ");
		System.out.print(calendar.get(Calendar.MINUTE) + "분 ");
		System.out.println(calendar.get(Calendar.SECOND) + "초");
		Date d = calendar.getTime();
		System.out.println(d);
		
		calendar.set(1997,0,26,25,00,30);
		System.out.print("내가 태어난 일시는 : ");
		System.out.print(calendar.get(Calendar.YEAR) + "년 ");
		System.out.print(calendar.get(Calendar.MONTH)+1+"월 ");
		System.out.print(calendar.get(Calendar.DATE) + "일 ");
		System.out.print(calendar.get(Calendar.HOUR) + "시 ");
		System.out.print(calendar.get(Calendar.MINUTE)+"분 ");
		System.out.println(calendar.get(Calendar.SECOND) + "초");
	}
}
