import java.util.*;

class QueueTest1 {
	public static void main(String args[]) {
		LinkedList<String> queue = new LinkedList<String>();
		System.out.println("ť�� ��⵵ offer : " + queue.offer("��⵵"));
		System.out.println("ť�� ��û�� offer : " + queue.offer("��û��"));
		System.out.println("ť�� ������ offer : " + queue.offer("������"));
		System.out.println("ť�� ���� offer : " + queue.offer("����"));
		System.out.println("ť�� ��� offer : " + queue.offer("���"));
		System.out.println("ť�� ���ֵ� offer : " + queue.offer("���ֵ�"));

		System.out.println("=============================");
		int n = queue.indexOf("���ֵ�");
		if (n != -1)
			System.out.println("���ÿ��� ���� \"���ֵ�\"�� ��ġ�� : "+n+"��° �Դϴ�");
		else
			System.out.println("���ÿ��� ���� \"���ֵ�\"�� �����ϴ�");
		System.out.println("=============================");
		while(!queue.isEmpty()) {
			Object obj = queue.poll();
			System.out.println("ť���� poll : " + obj);
		}
	}
}
