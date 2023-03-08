package school_4_2_1;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class week7homework2 {

	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		System.out.print("생일 입력(년월일을 공백으로 구분하여 입력) :");
		int year =s.nextInt();
		int month=s.nextInt();
		int day=s.nextInt();
		LocalDate birth =LocalDate.of(year, month, day);
		LocalDate today=LocalDate.now();
		System.out.println("당신의 생일은 : "+ toString(birth));
		System.out.println("오늘의 날짜는 : "+ toString(today));
		System.out.println("생일부터 오늘까지의 일 :" +birth.until(today,ChronoUnit.DAYS));
		System.out.println("생일부터 오늘까지의 년 :" +birth.until(today,ChronoUnit.YEARS));
		System.out.println("==========================================");
		LocalDate birth_100 =birth.plusYears(100);
		System.out.println("당신이 100살이 되는 날은 :"+toString(birth_100));
		System.out.println("100살까지 남은 주(week) 수 : " + today.until(birth_100,ChronoUnit.WEEKS));
		System.out.println("100살까지 남은 일 수 : " +today.until(birth_100,ChronoUnit.DAYS));
		System.out.println("==========================================");
		LocalDateTime current = LocalDateTime.now();
		LocalTime mid =LocalTime.of(0, 0);
		LocalDateTime midnight =LocalDateTime.of(today, mid);
		System.out.println("현재의 시간은 : " +current);
		System.out.println("오늘 자정까지 남은 시간(초) :"+midnight.until(current,ChronoUnit.SECONDS));
	}
	public static String toString(LocalDate d) {
		return d.getYear()+"년"+d.getMonthValue()+"월"+d.getDayOfMonth()+"일";
	}
		
		
		
		// TODO Auto-generated method stub

	}


