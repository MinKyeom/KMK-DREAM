package school_4_2_1;
import java.util.Scanner;

abstract class Calc{
	 int a;
	 int b;
	 void setValue(int a,int b) {}
	 int calculate() {return 0;}
	 
	}
	class Add extends Calc{
	 void setValue(int a,int b){
	  this.a=a;
	  this.b=b;
	 }
	 
	 int calculate(){
	  return a+b;
	 }
	}
	class Sub extends Calc{
	 void setValue(int a,int b){
	  this.a=a;
	  this.b=b;
	 }
	 
	 int calculate(){
	  return a-b;
	 }
	}
	 
	 class Mul extends Calc{
	  void setValue(int a,int b){
	   this.a=a;
	   this.b=b;
	  }
	  
	  int calculate(){
	   return a*b;
	  }
	 }
	 
	 class Div extends Calc{
	  void setValue(int a,int b){
	   this.a=a;
	   this.b=b;
	  }
	  
	  int calculate(){
	   return a/b;
	  }
	 }

public class week4homework  {
	 public static void main(String[] args) {
		  Scanner rd = new Scanner(System.in);	  
		  System.out.println("두 정수와 연산자를 입력하세요:");
		  
		  int a=rd.nextInt();
		  int b=rd.nextInt();
		 
		  System.out.println("연산 기호를 입력하세요:");
		  
		  String cc = rd.next();
		  char c=cc.charAt(0);
		  switch(c){
		  case '+':
		   Add plus = new Add();
		   plus.setValue(a, b);
		   System.out.println("덧셈의 결과는 "+plus.calculate()+" 입니다.");
		   break;
		   
		  case '-':
		   Sub sub = new Sub();
		   sub.setValue(a, b);
		   System.out.println("뺄셈의 결과는 "+sub.calculate()+" 입니다.");
		   break;
		   
		  case '*':
		   Mul mul = new Mul();
		   mul.setValue(a, b);
		   System.out.println("곱셉의 결과는 "+mul.calculate()+" 입니다.");
		   break;
		   
		  case '/':
		   Div div = new Div();
		   div.setValue(a, b);
		   System.out.println("나눗셈의 결과는 "+div.calculate()+" 입니다.");
		   break;
		  default:
			    System.out.println("잘못된 값입니다.");
			    break;		  		
			 }		 				  
		  }  				 
		 }
		
	 
