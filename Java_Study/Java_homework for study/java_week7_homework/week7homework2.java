package school_4_2_1;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class week7homework2 {

	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		System.out.print("���� �Է�(������� �������� �����Ͽ� �Է�) :");
		int year =s.nextInt();
		int month=s.nextInt();
		int day=s.nextInt();
		LocalDate birth =LocalDate.of(year, month, day);
		LocalDate today=LocalDate.now();
		System.out.println("����� ������ : "+ toString(birth));
		System.out.println("������ ��¥�� : "+ toString(today));
		System.out.println("���Ϻ��� ���ñ����� �� :" +birth.until(today,ChronoUnit.DAYS));
		System.out.println("���Ϻ��� ���ñ����� �� :" +birth.until(today,ChronoUnit.YEARS));
		System.out.println("==========================================");
		LocalDate birth_100 =birth.plusYears(100);
		System.out.println("����� 100���� �Ǵ� ���� :"+toString(birth_100));
		System.out.println("100����� ���� ��(week) �� : " + today.until(birth_100,ChronoUnit.WEEKS));
		System.out.println("100����� ���� �� �� : " +today.until(birth_100,ChronoUnit.DAYS));
		System.out.println("==========================================");
		LocalDateTime current = LocalDateTime.now();
		LocalTime mid =LocalTime.of(0, 0);
		LocalDateTime midnight =LocalDateTime.of(today, mid);
		System.out.println("������ �ð��� : " +current);
		System.out.println("���� �������� ���� �ð�(��) :"+midnight.until(current,ChronoUnit.SECONDS));
	}
	public static String toString(LocalDate d) {
		return d.getYear()+"��"+d.getMonthValue()+"��"+d.getDayOfMonth()+"��";
	}
		
		
		
		// TODO Auto-generated method stub

	}


