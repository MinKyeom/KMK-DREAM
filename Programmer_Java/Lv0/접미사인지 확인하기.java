// package Programmers;

// public class 접미사인지 확인하기 {
  
// }

// 출처: 프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181908

// 풀이 과정

/*
 * import java.util.*;

class Solution {
    public int solution(String my_string, String is_suffix) {
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
        if(check.contains(is_suffix)){
            return 1;
        }
        else{
            return 0;
        }
//         String[] answer = check.toArray(new String[0]);
//         Arrays.sort(answer); // 오름차순 정렬
        
//         if (answer.contains(is_suffix)){
//             return 1;
//         }
//         else {
//             return 0;
//         }
    }
}
 */
