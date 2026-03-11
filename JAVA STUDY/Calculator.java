public class Calculator {

  static double pie = 3.14;
  // int plus(int x , int y){
  //   int result = x+y;
  //   return result;
  // }
  

  static int plus(int x, int y){
    return x+y;
  }

  double avg(int x, int y){
    double sum = plus(x,y);
    double result =sum/2;
    return result;
  }

  void execute(){
    double result = avg(7,10);
    println("실행결과"+result);
  }

  void println(String message){
    System.out.println(message);
  }

}
