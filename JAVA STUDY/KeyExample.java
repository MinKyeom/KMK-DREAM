import java.util.*;

public class KeyExample {
  public static void main(String[] args){
    //Key 객체를 식별키로 사용해, String 값을 저장하는 HashMap 객체 생성
    HashMap<Key, String> hashMap = new HashMap<Key, String>();

    // 식별키 new Key(1)에 길동 저장
    hashMap.put(new Key(1), "길동");

    String value = hashMap.get(new Key(1));
    System.out.println(value);
  }
}
/*
HashMap 동작 원리
[유저가 데이터를 넣음] 
"길동" 이라는 객체를 HashMap에 저장해줘!
      │
      ▼
[HashMap의 행동]
1. "길동" 객체의 hashCode() 메서드를 호출한다. -> 결과: (예) 12345
2. 12345라는 숫자를 가공해서 '3번 서랍'이라는 내부 주소를 계산한다.
3. 3번 서랍에 "길동" 객체를 안전하게 보관한다.
 */