import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*;

class JButton1 extends JFrame {
	public JButton1() {
		ImageIcon korea = new ImageIcon("korea1.gif");
		ImageIcon usa = new ImageIcon("usa.gif");
		ImageIcon germany = new ImageIcon("germany.gif");
		JButton nat = new JButton(korea);
		nat.setPressedIcon(usa);
		nat.setRolloverIcon(germany);
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		ct.add(nat);
		setTitle("JButton Test1");
		setSize(500,400);
		setVisible(true);
	}
}
public class JButtonTest1 {
	public static void main(String[] args) {
		new JButton1();
	}
}
