// package Programmers;

// public class 문자 개수 세기 {
  
// }

// 출처: 프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181902

// 풀이 과정

/*
 *class Solution {
    public int[] solution(String my_string) {
        String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        String[] alpha_list = alpha.split("");
        
        String[] split_my_string = my_string.split(""); 
        int[] answer = new int[52];
        
        for(String i:split_my_string){
            for(int k = 0; k<alpha_list.length; k++){
                // System.out.println("check1:"+alpha_list[k]);
                // System.out.println(i);
                
                if(i.equals(alpha_list[k])){
                    // System.out.println("if는?");
                    answer[k]+=1;
                }
            }
            
        }
        
        return answer;
    }
}
 */
