import javax.swing.*; 
import java.awt.*; 
import java.awt.event.*; 
import java.io.*;

class GUI2 extends JFrame implements  ActionListener {
	private JTextField jtf;
	private JTextArea jta;
	
	public GUI2() {
		JButton jb = new JButton("파일 읽어오기");
		jtf = new JTextField("파일이름을 입력하세요",20);
		jta = new JTextArea(10,20);
		jta.setEditable(false);
		Container ct = getContentPane();
		ct.setLayout(new FlowLayout());
		JPanel p1 = new JPanel();
		p1.add(jtf);
		p1.add(jb);
		ct.add(p1);
		ct.add(jta);
		jb.addActionListener(this);
		setTitle("GUI Test2");
		setSize(400,400);
		setVisible(true);
	}
	public void actionPerformed(ActionEvent ae) {
		try {
			String s = jtf.getText();
			FileInputStream fis = new FileInputStream(s);
			DataInputStream dis = new DataInputStream(fis);
			jta.setText(dis.readUTF());
			fis.close();
			System.out.print(s + "파일을 읽었습니다");
			}
		catch(Exception e) {
			System.out.print("파일이 존재하지 않습니다");
		}
	}
}
public class GUITest2 {
	public static void main(String[] args) {
		new GUI2();
	}
}