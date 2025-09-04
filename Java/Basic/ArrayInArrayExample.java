package src.Java_Basic;

public class ArrayInArrayExample {
  public static void main(String[] args){

    int[][] mathScore = new int[2][3];
    for(int i = 0; i< mathScore.length; i++){
      for(int k=0; k<mathScore.length; k++){
        System.out.println("mathScore["+i+"]["+"]="+mathScore[i][k]);
      }
    }
    System.out.println(); 
  }

  int[][] englishScore = new int[2][];
  
}
