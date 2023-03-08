import javax.swing.*; 
import java.awt.*; 
class JScrollPane1 extends JFrame {
	public JScrollPane1() {
		Container ct = getContentPane();
		JPanel jp = new JPanel();
		jp.setLayout(new GridLayout(20,5));
		for(int i = 1 ; i <=100 ; i++ )	
			jp.add(new JButton(i + "¹ø"));		
		int v = ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED;
		int h = ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED;
		JScrollPane jsp = new JScrollPane(jp, v, h);
		ct.add(jsp, BorderLayout.CENTER);
		setTitle("JScrollPane Test1");
		setSize(300,300);
		setVisible(true);
	}
}
public class JScrollPaneTest1 {
	public static void main(String[] args) {
		new JScrollPane1();
	}
}