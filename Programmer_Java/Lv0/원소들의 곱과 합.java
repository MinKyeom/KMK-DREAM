// package Programmers;

// public class 원소들의 곱과 합 {
  
// }

// 출처:프로그래머스
// https://school.programmers.co.kr/learn/courses/30/lessons/181929

class Solution {
    public int solution(int[] num_list) {
        int num_len = num_list.length;
        int num_sum = 0;
        int num_mul = 1;
        for(int i=0; i<num_len; i++){
            num_sum+=num_list[i];
            num_mul*=num_list[i];
            
        }
        double num_sum_2 = Math.pow(num_sum,2);
        if( (int)num_sum_2 > num_mul){
            return 1;
        }
        else {
            return 0;
        }
    }
}