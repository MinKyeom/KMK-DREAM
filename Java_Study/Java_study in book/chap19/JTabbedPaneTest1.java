import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class RadioPanel extends JPanel implements ActionListener {
	JLabel jl1 = new JLabel("당신의 성별은? ");
	JLabel jl2 = new JLabel("");
	public RadioPanel() {
		JRadioButton jrb1 = new JRadioButton("남자");
		JRadioButton jrb2 = new JRadioButton("여자");
		add(jl1);
		add(jl2);
		add(jrb1);
		add(jrb2);
		jrb1.addActionListener(this);
		jrb2.addActionListener(this);
	}
	public void actionPerformed(ActionEvent ae) {
		String s = ae.getActionCommand();
		jl2.setText(s);
	}
}

class ComboPanel extends JPanel implements ItemListener {
	JLabel jl1 = new JLabel("당신의 혈액형은? ");
	JLabel jl2 = new JLabel("");
	public ComboPanel() {
		JComboBox jcb = new JComboBox();
		jcb.addItem("A형");
		jcb.addItem("B형");
		jcb.addItem("AB형");
		jcb.addItem("O형");
		add(jl1);
		add(jl2);
		add(jcb);
		jcb.addItemListener(this);
	}
	public void itemStateChanged(ItemEvent ie) {
		Object s = ie.getItem();
		jl2.setText(s.toString());
	}
}

class JTabbedPane1 extends JFrame {
	public JTabbedPane1() {
		JTabbedPane jtp = new JTabbedPane();
		RadioPanel rp = new RadioPanel();
		ComboPanel cp = new ComboPanel();
		jtp.addTab("성별", rp);
		jtp.addTab("혈액형", cp);
		getContentPane().add(jtp);
		setTitle("JTabbedPaneTest1");
		setSize(500,150);
		setVisible(true);
	}
}

public class JTabbedPaneTest1 {
	public static void main(String[] args) {
		new JTabbedPane1();
	}
}