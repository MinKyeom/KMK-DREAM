// package Programmers;

// public class 접두사인지 확인하기 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181906

//풀이 과정
/*
 * import java.util.*;

class Solution {
    public int solution(String my_string, String is_prefix) {
        List<String> prefix = new ArrayList<>();
        String[] split_string = my_string.split("");
        
        for(String i: split_string){
            int now_len = prefix.size();
            if(now_len==0){
                prefix.add(i);
                continue;
            }
            String last_word = prefix.get(now_len-1);
            String new_word = last_word+i;
            prefix.add(new_word);
        }
        
        for(String word:prefix){
            if( word.equals(is_prefix) ){
                System.out.print(my_string);
                return 1;
            }
        }
        System.out.print(prefix);
        return 0;
        
    }
}
 */


// 풀이과정_개선 중 

/*
 * import java.util.*;

class Solution {
    public int solution(String my_string, String is_prefix) {
        List<String> prefix = new ArrayList<>();
        String[] split_string = my_string.split("");
        
        for(String i: split_string){
            int now_len = prefix.size();
            if(now_len==0){
                prefix.add(i);
                continue;
            }
            String last_word = prefix.get(now_len-1);
            String new_word = last_word+i;
            prefix.add(new_word);
        }
        
        for(String word:prefix){
            if( word.equals(my_string) ){
                System.out.print(word);
                return 1;
            }
        }
        System.out.print(prefix);
        return 0;
        
    }
}
 */