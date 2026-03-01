public class SwitchExample {
  public static void main(String[] args){
    // int num = (int) (Math.random() * 6 ) + 1;
    int num = 2;
    // System.out.println(num);
    
    switch(num){
      case 1:
        System.out.println(num);
        break;
      case 2:
        System.out.println("흠");
      
      default:
        System.out.println("여기인가");
      }
  }
}
