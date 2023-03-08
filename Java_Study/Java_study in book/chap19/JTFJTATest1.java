import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*; 

class JTFJTA1 extends JFrame implements  ActionListener {
	private JTextField jtf;
	private JTextArea jta;
	private JLabel jl = new JLabel("입력하십시요");
	public JTFJTA1() {
		jtf = new JTextField(20);
		jta = new JTextArea(10,20);
		jta.setEditable(false);
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		JPanel p1 = new JPanel();
		p1.add(jtf);
		p1.add(jta);
		ct.add(p1);
		ct.add(jl);
		ct.add(jl);
		jtf.addActionListener(this);
		setTitle("JTextField,JTextArea Test1");
		setSize(500,300);
		setVisible(true);
	}
	public void actionPerformed(ActionEvent ae) {
		if(jta.getLineCount() <= jta.getRows()) {
			jta.append(ae.getActionCommand()+"\n");
			jtf.setText("");
		} else {
			jl.setText("입력이 종료되었습니다");
			jtf.setEditable(false);
		}
	}
}
public class JTFJTATest1 {
	public static void main(String[] args) {
		new JTFJTA1();
	}
}