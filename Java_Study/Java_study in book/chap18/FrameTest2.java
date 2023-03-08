import javax.swing.*; 
import java.awt.*;

class FirstFrame3 extends JFrame  {
	public FirstFrame3(){
		Container ct = getContentPane();
		JButton jb = new JButton("테스트버튼");
		ct.add(jb);
		setTitle("세 번째 GUI 프로그램");
		setSize(400,300);
		setVisible(true);		
	}	
}
public class FrameTest2{	
	public static void main(String[] args) {
		new FirstFrame3();
  }
}