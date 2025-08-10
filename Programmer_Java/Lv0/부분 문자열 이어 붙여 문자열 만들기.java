// package Programmers;

// public class 부분 문자열 이어 붙여 문자열 만들기 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181911

// 풀이 과정
/*
 * class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        int i = 0;
        for(String string_section: my_strings ){
            String[] split_section = string_section.split("");
            int s = parts[i][0];
            int e = parts[i][1];
            i++;
            for(int k = s; k<=e; k++){
                answer+=split_section[k];
            }
        }
        return answer;
    }
}
 */
