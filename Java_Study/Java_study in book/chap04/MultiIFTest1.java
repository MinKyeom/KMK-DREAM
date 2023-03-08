import java.util.Scanner;
public class MultiIFTest1 {
	public static void main(String args[]) 
	{
		Scanner stdin = new Scanner(System.in);
		System.out.print("¼ºÀûÀ» ÀÔ·ÂÇÏ¼¼¿ä : ");
		int grade = stdin.nextInt();
		if (grade >= 90)
			System.out.println("AÇÐÁ¡ Ãëµæ");
		else if (grade >= 80)
			System.out.println("BÇÐÁ¡ Ãëµæ");	
		else if (grade >= 70)
			System.out.println("CÇÐÁ¡ Ãëµæ");
		else if (grade >= 60)
			System.out.println("DÇÐÁ¡ Ãëµæ");
		else 
			System.out.println("ÇÐÁ¡ Ãëµæ ½ÇÆÐ");
	}
}