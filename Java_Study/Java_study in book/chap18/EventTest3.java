import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*;

class EventClass implements ActionListener {
	JLabel jl;
	public EventClass(JLabel jl){
		this.jl = jl;		
	}
	public void actionPerformed(ActionEvent e) {
		jl.setText(e.getActionCommand());
	}		
}
class Event3 extends JFrame { 
	JLabel jl;
	JButton jb1, jb2;
	public Event3() {
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		jb1 = new JButton("사랑합니다");
		jb2 = new JButton("행복합니다");
		jl = new JLabel("버튼을 누르세요");
		jb1.addActionListener(new EventClass(jl));
		jb2.addActionListener(new EventClass(jl));
		ct.add(jb1);
		ct.add(jb2);
		ct.add(jl);		
		setTitle("Event Test3");
		setSize(250,150);
		setVisible(true);
	}
	
}  
public class EventTest3 {
	public static void main(String[] args) {
		new Event3();
	}
}