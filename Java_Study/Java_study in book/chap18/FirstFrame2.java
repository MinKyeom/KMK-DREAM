import javax.swing.*; 
import java.awt.*;

public class FirstFrame2 {
	public FirstFrame2(){
		JFrame jf = new JFrame("두 번째 GUI 프로그램");
		Container ct = jf.getContentPane();
		JButton jb = new JButton("테스트버튼");
		ct.add(jb);
		jf.setSize(400,300);
		jf.setVisible(true);		
	}
	public static void main(String[] args) {
		new FirstFrame2();
	}
}
