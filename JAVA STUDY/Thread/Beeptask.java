package Thread;

import java.awt.Toolkit;

public class Beeptask implements Runnable {
    public void run(){
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        for(int i = 0; i < 5; i++){
            System.out.println("check");
        }
    }
    
}
