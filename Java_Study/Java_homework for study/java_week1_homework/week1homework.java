package school_4_2_1;

class BoxClass
{
 int width;
 int height;
 int depth;
 double d_width,d_height,d_depth;

public BoxClass(int width, int height, int depth)
	{
	this.width=width;
	this.height=height;
	this.depth=depth;	
	}
public BoxClass()
	{
		this.width=10;
	}
public BoxClass(double d_width, double d_height,double d_depth)
	{
		this.d_width=d_width;
		this.d_height=d_height;
		this.d_depth=d_depth;
		
		
		
	}
}


public class week1homework {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		BoxClass obj1=new BoxClass(10,20,30);
		int result=obj1.width*obj1.height*obj1.depth;
		System.out.println(result);
		
		BoxClass obj2=new BoxClass();
		System.out.println(obj2.width);
		
		BoxClass obj3=new BoxClass(10.3,20.4,30.2);
		double d_result=obj3.d_width*obj3.d_height*obj3.d_depth;
		System.out.println(d_result);
		
		

	}

}
