public class Student extends People{

  public int StudentNo;
  
  public Student(String name,String ssn, int StudentNo){
    super(name,ssn);
    this.StudentNo = StudentNo;
  }
}
