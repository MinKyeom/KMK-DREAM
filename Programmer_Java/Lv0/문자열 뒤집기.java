// package Programmers;

// public class 문자열 뒤집기 {
  
// }


// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181905


// 풀이과정_개선 중 
/*
 * class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        String[] split_string = my_string.split("");
        
        int string_len = split_string.length;
        
        String[] before = new String[string_len];
        
        // 깊은 배열 복사
        for(int k=0; k < string_len; k++ ){
            before[k] = split_string[k];
            
        }
        
        for( int t =0; t<string_len; t++){
            if(t>=s && t<=e){
                answer+=split_string[string_len-t+s-1];
            }
            else{
                answer+=split_string[t];
            }
        }
        
        return answer;
    }
}
 */