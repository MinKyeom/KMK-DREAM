// package Programmers;

// public class 문자열 여러번 뒤집기 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181913

// 풀이과정
/*
 * class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        String[] string_split = my_string.split("");
        String after_str = "";
        int start;
        for(int[] check_index:queries){
            int s = check_index[0];
            int e = check_index[1];
            after_str ="";
            String now_str = "";
            for(int i=e; i>=s; i--){
                now_str = string_split[i];
                after_str +=now_str;
            }
            
            start = s;
            for(String change_str:after_str.split("")){
                string_split[start] = change_str;
                start++;
            }
            
        
        }
        for(String sum_alpha: string_split){
            answer+=sum_alpha;
        }
        
        return answer;
    }
}
 */

//풀이과정_개선중
/*
 * class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        String[] string_split = my_string.split("");
        String after_str = "";
        int start;
        for(int[] check_index:queries){
            int s = check_index[0];
            int e = check_index[1];
            after_str ="";
            String now_str = "";
            for(int i=e; i>=s; i--){
                now_str = string_split[e];
                after_str +=now_str;
            
            start = s;
            for(String change_str:after_str.split("")){
                string_split[start] = change_str;
            }
            }
        
        }
        for(String sum_alpha: string_split){
            answer+=sum_alpha;
        }
        
        return answer;
    }
}
 */