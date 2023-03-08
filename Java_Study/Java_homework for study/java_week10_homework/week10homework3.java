package school_4_2_1;

import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*; 

class JComboBox1 extends JFrame implements ItemListener {
	JLabel jl;
	public JComboBox1() {
		jl = new JLabel();
		JComboBox jcb = new JComboBox();
		String fr[] = {"AFREECA","DRX","KT","ROX","T1"}; 
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout()); 
		for(int i = 0 ; i < 5 ; i++){
			jcb.addItem(fr[i]);
		}
		ct.add(jcb);
		ct.add(jl);
		jcb.addItemListener(this);
		setTitle("JComboBox Test1");
		setSize(200,200);
		setVisible(true);
	}
	public void itemStateChanged(ItemEvent ie) {
		String fruit = (String)ie.getItem();
		jl.setIcon(new ImageIcon(fruit+".png"));
	}
}
public class week10homework3 {
	public static void main(String[] args) {
		new JComboBox1();
	}
}