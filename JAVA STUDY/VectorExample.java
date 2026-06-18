import java.util.*;


public class VectorExample {
  public static void main(String[] args){
    List<Board> list = new Vector<Board>();

    list.add(new Board("제목1", "내용1", "글쓴이1"));

    for(int i = 0; i<list.size(); i++){

      Board board = list.get(i);
      System.out.println(board.subject+" "+board.content+" "+board.writer);
    }

  } 
   
}
