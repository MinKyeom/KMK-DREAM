package school_4_2_1;
import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*;

class JButton2 extends JFrame implements ActionListener {
	JTextField jtf;
	public JButton2() {
		jtf = new JTextField(10);
		ImageIcon AFREECA = new ImageIcon("AFREECA.png");
		ImageIcon DRX = new ImageIcon("DRX.png");
		ImageIcon KT = new ImageIcon("KT.png");
		ImageIcon ROX = new ImageIcon("ROX.png");
		ImageIcon T1 = new ImageIcon("T1.png");
		JButton jb1 = new JButton("아프리카",AFREECA);
		JButton jb2 = new JButton("DRX",DRX);
		JButton jb3 = new JButton("KT",KT);
		JButton jb4 = new JButton("ROX",ROX);
		JButton jb5 = new JButton("T1",T1);
		Container ct = getContentPane();
		ct.setLayout(new GridLayout(3,2));
		ct.add(jb1);
		ct.add(jb2);
		ct.add(jb3);
		ct.add(jb4);
		ct.add(jb5);
		ct.add(jtf);
		jb1.addActionListener(this);
		jb2.addActionListener(this);
		jb3.addActionListener(this);
		jb4.addActionListener(this);
		jb5.addActionListener(this);
		setTitle("JButton Test2");
		setSize(200,200);
		setVisible(true);
	}
	public void actionPerformed(ActionEvent ae) {
		jtf.setText(ae.getActionCommand());
	}
}

public class week9homework1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new JButton2();
	}

}
