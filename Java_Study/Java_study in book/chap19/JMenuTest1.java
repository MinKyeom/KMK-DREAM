import javax.swing.*; 
import java.awt.event.*;
import java.awt.*; 

class JMenu1 extends JFrame implements ActionListener {
	JTextField jtf;
	public JMenu1() {
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		JMenuBar jmb = new JMenuBar();
		JMenu menu1 = new JMenu("파일");
		JMenu menu2 = new JMenu("편집");
		JMenuItem jmi = new JMenuItem("새파일");
		jmi.addActionListener(this);
		menu1.add(jmi);
		jmi = new JMenuItem("저장하기");
		jmi.addActionListener(this);
		menu1.add(jmi);
		jmb.add(menu1);
		jmi = new JMenuItem("열기");
		jmi.addActionListener(this);
		menu2.add(jmi);
		jmi = new JMenuItem("잘라내기");
		jmi.addActionListener(this);
		menu2.add(jmi);
		jmi = new JMenuItem("복사");
		jmi.addActionListener(this);
		menu2.add(jmi);
		JCheckBoxMenuItem jcbmi = new JCheckBoxMenuItem("눈금자");
		jcbmi.addActionListener(this);
		menu2.add(jcbmi);
		JRadioButtonMenuItem jrbmb = new JRadioButtonMenuItem("수정가능상태");
		jrbmb.addActionListener(this);
		menu2.add(jrbmb);
		jmb.add(menu2);
		setJMenuBar(jmb);
		jtf = new JTextField();
		c.add(jtf, BorderLayout.SOUTH);
		setTitle("JMenuTest1");
		setSize(300,200);
		setVisible(true);
	}
	public void actionPerformed(ActionEvent ae) {
		jtf.setText(ae.getActionCommand());
	}
}
public class JMenuTest1 {
	public static void main(String[] args) {
		new JMenu1();
	}
}