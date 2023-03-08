package school_4_2_1;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;


public class week7homework1 {

	public static void main(String[] args) {
		LocalDate date= LocalDate.now();
		LocalTime time= LocalTime.now();
		LocalDateTime dt =LocalDateTime.now();
		System.out.println("오늘의 날씨 : "+date);
		System.out.println("현재의 시간 : "+time);
		System.out.println("현재의 날짜와 시간 "+dt);
		String s=dt.getYear()+"년";
		s+=dt.getMonthValue()+"월";
		s+=dt.getDayOfWeek()+"일";
		s+=dt.getHour()+"시";
		s+=dt.getMinute()+"분";
		s+=dt.getSecond()+"초";
		System.out.println("현재의 날짜와 시간"+s);
		
		System.out.println("오늘부터 100일 기념일 :"+date.plusDays(100));
		System.out.println("오늘부터 10주 후의 날짜" +date.plusWeeks(10));
		
		// TODO Auto-generated method stub

	}

}
