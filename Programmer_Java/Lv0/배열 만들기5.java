// package Programmers;

// public class 배열 만들기5 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181912
//풀이 과정_개선 중
/*
 * // String을 분리한 이후(split) > 해당 범위 문자열 합치기
// > 범위 비교 후 미리 만들어놓은 리스트에 넣은 후 > 최종 배열로 변환한 후 return 
import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        int[] answer = {};
        List<Integer> result_check = new ArrayList<>();
        
        for(String str_check: intStrs){
            String check = "";
            String[] split_str =str_check.split("");
            for(int i = s; i<(i+l); i++){
                check+=split_str[i];
            }
            int num = Integer.parseInt(check);
            if(num > k){
                result_check.add(num);
            }
        
        }
        System.out.print(result_check);
        return answer;
    }
}

 */

//풀이 과정_개선 중
/*
 * 
// String을 분리한 이후(split) > 해당 범위 문자열 합치기
// > 범위 비교 후 미리 만들어놓은 리스트에 넣은 후 > 최종 배열로 변환한 후 return 

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        int[] answer = {};
        
        for(String check: intStrs){
        }
        return answer;
    }
}

 */