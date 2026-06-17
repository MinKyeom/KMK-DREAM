import java.util.*;

public class ArrayListExample {

  public static void main(String[] args){
    List<String> list = new ArrayList<String>();

    list.add("Java");
    list.add("Jdbc");

    int size = list.size();
    System.out.println("총 객체 수"+size);

    String skill = list.get(1);
    System.out.println("2번째 객체 "+ skill);

    for(int i = 0; i<list.size(); i++){
      String str = list.get(i);
      System.out.println("객체"+str);
    }

    list.remove(1);
    // list.remove("Jdbc");

    for(int i = 0; i<list.size(); i++){
      String str = list.get(i);
      System.out.println("지우고 난 이후 객체"+str);
    }
  }
}
