package Thread;

public class BeepPrintExample2 {
    public static void main(String[] args){
    
        Runnable beeptask = new Beeptask();
        Thread thread = new Thread(beeptask);
        thread.start();

        for(int i = 0; i<5; i++){
            System.out.println("check2");
            try{Thread.sleep(100);}
            catch(Exception e){};
        }
    
  }
}
