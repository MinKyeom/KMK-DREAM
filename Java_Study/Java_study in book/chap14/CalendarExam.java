import java.util.Calendar;
import java.util.Date;

class CalendarExam {
	public static void main(String args[]) {
		Calendar calendar = Calendar.getInstance();
		System.out.print("��¥ : ");
		System.out.print(calendar.get(Calendar.YEAR) + "�� ");
		System.out.print(calendar.get(Calendar.MONTH)+1+"�� ");
		System.out.print(calendar.get(Calendar.DATE) + "�� ");
		System.out.print(calendar.get(Calendar.HOUR) + "�� ");
		System.out.print(calendar.get(Calendar.MINUTE) + "�� ");
		System.out.println(calendar.get(Calendar.SECOND) + "��");
		Date d = calendar.getTime();
		System.out.println(d);
		
		calendar.set(1997,0,26,25,00,30);
		System.out.print("���� �¾ �Ͻô� : ");
		System.out.print(calendar.get(Calendar.YEAR) + "�� ");
		System.out.print(calendar.get(Calendar.MONTH)+1+"�� ");
		System.out.print(calendar.get(Calendar.DATE) + "�� ");
		System.out.print(calendar.get(Calendar.HOUR) + "�� ");
		System.out.print(calendar.get(Calendar.MINUTE)+"�� ");
		System.out.println(calendar.get(Calendar.SECOND) + "��");
	}
}
