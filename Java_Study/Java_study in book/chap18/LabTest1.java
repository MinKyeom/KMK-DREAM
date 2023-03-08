import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*;

class Lab1 extends JFrame { 
	JLabel jl;
	public Lab1() {
		JButton jb1, jb2, jb3, jb4;
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		jb1 = new JButton("1학년");
		jb2 = new JButton("2학년");
		jb3 = new JButton("3학년");
		jb4 = new JButton("4학년");
		jl = new JLabel("버튼을 누르세요");
		jb1.addActionListener(new EventProcess());
		jb2.addActionListener(new EventProcess());
		jb3.addActionListener(new EventProcess());
		jb4.addActionListener(new EventProcess());;
		ct.add(jb1);
		ct.add(jb2);
		ct.add(jb3);
		ct.add(jb4);		
		ct.add(jl);		
		setTitle("Lab Test1");
		setSize(300,150);
		setVisible(true);
	}
	private class EventProcess implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			jl.setText(e.getActionCommand());
		}		
	}
}  
public class LabTest1 {
	public static void main(String[] args) {
		new Lab1();
	}
}