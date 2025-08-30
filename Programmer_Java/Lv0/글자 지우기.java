// package Programmers;

// public class 글자 지우기 {
  
// }

// 출처: 프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181900

// 풀이 과정
/*
 * class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        
        String[] split_string = my_string.split("");
        
        for(int i = 0; i<split_string.length; i++){
            Boolean flag = false;
            
            for(int k: indices){
                if(i==k){
                    flag =true;
                }
            }
            if(flag == false){
                answer+=split_string[i];
            }
            
        }
        
        
        return answer;
    
    
    }
}
 */