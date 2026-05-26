// public class SmartPhone extends Phone {
//   public SmartPhone(String owner){
//     super(owner);
//   }

//   public void internetSearch(){
//     System.out.println("인터넷 검색을 합니다.");
//   }
// }

public class SmartPhone {
    private String company;
    private String os;

    // 생성자
    public SmartPhone(String company, String os){
      this.company = company;
      this.os = os;
    }

    @Override
    public String toString(){
      return company + "," + os;
    }
}