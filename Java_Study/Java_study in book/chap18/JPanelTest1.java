import javax.swing.*; 
import java.awt.*; 

class JPanel1 extends JFrame{
	public JPanel1() {
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		ct.add(new JRadioButton("자바"));
		ct.add(new JRadioButton("C"));
		ct.add(new JRadioButton("VisualBasic"));
		ct.add(new JRadioButton("JSP"));
		ct.add(new JRadioButton("PHP"));
		ct.add(new JButton("자바"));
		ct.add(new JButton("C"));
		ct.add(new JButton("VisualBasic"));
		ct.add(new JButton("JSP"));
		ct.add(new JButton("PHP"));
		setTitle("JPanel Test1");
		setSize(300,200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true); 
  }
}
 public class JPanelTest1 {
  public static void main(String[] args) {
    new JPanel1();
  }
}	
