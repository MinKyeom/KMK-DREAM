import javax.swing.*; 
import java.awt.*;

class FirstFrame1 {
	public FirstFrame1(){
		JFrame jf = new JFrame("첫 번째 GUI 프로그램");
		Container ct = jf.getContentPane();
		JButton jb = new JButton("테스트버튼");
		ct.add(jb);
		jf.setSize(400,300);
		jf.setVisible(true);		
	}	
}
public class FrameTest1{	
	public static void main(String[] args) {
		new FirstFrame1();
  }
}