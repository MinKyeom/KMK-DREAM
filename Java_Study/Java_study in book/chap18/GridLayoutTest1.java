import javax.swing.*; 
import java.awt.*; 

class GridLayout1 extends JFrame{
	public GridLayout1(){
		Container ct = getContentPane();
		GridLayout gl = new GridLayout(4,5,10,10);
		ct.setLayout(gl);
		for ( int i = 1; i<=20 ; i++)
			ct.add(new JButton("¹öÆ°"+i));
		setTitle("GridLayout Test1");
		setSize(800,800);
		setVisible(true);
	}
}
public class GridLayoutTest1 {
	public static void main(String[] args) {
		new GridLayout1();
	}
}
