// package Programmers;

// public class 접미사 배열 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181909

/*
 * import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        Deque<String> check = new ArrayDeque<>();
        String[] split_string = my_string.split("");
        
        for(String s:split_string){
            int k = 0 ;
            while(k<check.size()){
                String first = check.removeFirst();
                first+=s;
                check.addLast(first);
                k++;
            }
            check.addFirst(s);
        }
        
        String[] answer = check.toArray(new String[0]);
        Arrays.sort(answer); // 오름차순 정렬
        return answer;
    }
}
 */