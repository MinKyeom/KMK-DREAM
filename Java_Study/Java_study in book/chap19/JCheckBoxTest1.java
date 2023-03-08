import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*; 
class JCheckBox1 extends JFrame implements ItemListener {
	JTextField jtf;
	public JCheckBox1() {
		jtf = new JTextField(10);
		JCheckBox jc1 = new JCheckBox("JSP");
		JCheckBox jc2 = new JCheckBox("PHP");
		JCheckBox jc3 = new JCheckBox("ASP");
		JCheckBox jc4 = new JCheckBox("Servlet");
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		ct.add(jc1);
		ct.add(jc2);
		ct.add(jc3);
		ct.add(jc4);
		ct.add(jtf);
		jc1.addItemListener(this);
		jc2.addItemListener(this);
		jc3.addItemListener(this);
		jc4.addItemListener(this);
		setTitle("JCheckBox Test1");
		setSize(250,100);
		setVisible(true);
	}
	public void itemStateChanged(ItemEvent ie) {
		jtf.setText(((JCheckBox)ie.getItem()).getText());
	}
} 
public class JCheckBoxTest1 {
	public static void main(String[] args) {
		new JCheckBox1();
	}
}
