import javax.swing.*; 
import java.awt.*; 

class BorderLayout1 extends JFrame{ 
	public BorderLayout1() {
		Container ct = getContentPane();
		BorderLayout bl = new BorderLayout(10, 10);
		ct.setLayout(bl);
		ct.add(new JButton("오른쪽버튼"), BorderLayout.EAST);
		ct.add(new JButton("왼쪽버튼"), BorderLayout.WEST);
		ct.add(new JButton("위쪽버튼"), BorderLayout.NORTH);
		ct.add(new JButton("아래쪽버튼"), BorderLayout.SOUTH);
		ct.add(new JButton("중앙버튼"), BorderLayout.CENTER);
		setTitle("BorderLayout Test1");
		setSize(400,300);
		setVisible(true);
	}
}  
public class BorderLayoutTest1 {
	public static void main(String[] args) {
		new BorderLayout1();
	}
}