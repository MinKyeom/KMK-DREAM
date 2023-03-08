import java.util.*;

class GCalendarExam1 {
	public static void main(String args[]) {
		String[] whatDay = {"","�Ͽ���","������","ȭ����","������","�����","�ݿ���","�����"};
		Scanner s = new Scanner(System.in);
		System.out.print("���� �Է�(������� �������� �����Ͽ� �Է�) : ");
		int year = s.nextInt();
		int month = s.nextInt();
		int day = s.nextInt();
		GregorianCalendar birth = new GregorianCalendar(year,month-1,day);
		GregorianCalendar today = new GregorianCalendar();
		long diff = (today.getTimeInMillis()-birth.getTimeInMillis())/1000;
		System.out.println("����� ������ "+printYMD(birth) + whatDay[birth.get(birth.DAY_OF_WEEK)]);
		System.out.println("������ "+printYMD(today) + whatDay[today.get(today.DAY_OF_WEEK)]);
		System.out.println("�¾�� ���ݱ��� "+diff/(24*60*60)+"���� �������ϴ�");
		System.out.println("�¾�� ���ݱ��� "+diff/(60*60)+"�ð��� �������ϴ�");
		birth.roll(Calendar.YEAR, 19);
		System.out.println("������ �Ǵ� �ش� : "+birth.get(birth.YEAR)+"�� �Դϴ�");
	}
	
	public static String printYMD(Calendar c) {
		return c.get(c.YEAR)+"�� "+(c.get(c.MONTH)+1)+"�� "+c.get(c.DATE)+"�� ";
	}
}