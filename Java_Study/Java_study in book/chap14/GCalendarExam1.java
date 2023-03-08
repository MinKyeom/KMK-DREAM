import java.util.*;

class GCalendarExam1 {
	public static void main(String args[]) {
		String[] whatDay = {"","일요일","월요일","화요일","수요일","목요일","금요일","토요일"};
		Scanner s = new Scanner(System.in);
		System.out.print("생일 입력(년월일을 공백으로 구분하여 입력) : ");
		int year = s.nextInt();
		int month = s.nextInt();
		int day = s.nextInt();
		GregorianCalendar birth = new GregorianCalendar(year,month-1,day);
		GregorianCalendar today = new GregorianCalendar();
		long diff = (today.getTimeInMillis()-birth.getTimeInMillis())/1000;
		System.out.println("당신의 생일은 "+printYMD(birth) + whatDay[birth.get(birth.DAY_OF_WEEK)]);
		System.out.println("오늘은 "+printYMD(today) + whatDay[today.get(today.DAY_OF_WEEK)]);
		System.out.println("태어나서 지금까지 "+diff/(24*60*60)+"일이 지났습니다");
		System.out.println("태어나서 지금까지 "+diff/(60*60)+"시간이 지났습니다");
		birth.roll(Calendar.YEAR, 19);
		System.out.println("성년이 되는 해는 : "+birth.get(birth.YEAR)+"년 입니다");
	}
	
	public static String printYMD(Calendar c) {
		return c.get(c.YEAR)+"년 "+(c.get(c.MONTH)+1)+"월 "+c.get(c.DATE)+"일 ";
	}
}