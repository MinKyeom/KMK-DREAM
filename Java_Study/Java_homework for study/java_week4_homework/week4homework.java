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
		  System.out.println("�� ������ �����ڸ� �Է��ϼ���:");
		  
		  int a=rd.nextInt();
		  int b=rd.nextInt();
		 
		  System.out.println("���� ��ȣ�� �Է��ϼ���:");
		  
		  String cc = rd.next();
		  char c=cc.charAt(0);
		  switch(c){
		  case '+':
		   Add plus = new Add();
		   plus.setValue(a, b);
		   System.out.println("������ ����� "+plus.calculate()+" �Դϴ�.");
		   break;
		   
		  case '-':
		   Sub sub = new Sub();
		   sub.setValue(a, b);
		   System.out.println("������ ����� "+sub.calculate()+" �Դϴ�.");
		   break;
		   
		  case '*':
		   Mul mul = new Mul();
		   mul.setValue(a, b);
		   System.out.println("������ ����� "+mul.calculate()+" �Դϴ�.");
		   break;
		   
		  case '/':
		   Div div = new Div();
		   div.setValue(a, b);
		   System.out.println("�������� ����� "+div.calculate()+" �Դϴ�.");
		   break;
		  default:
			    System.out.println("�߸��� ���Դϴ�.");
			    break;		  		
			 }		 				  
		  }  				 
		 }
		
	 
