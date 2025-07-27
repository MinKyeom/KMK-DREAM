// package Programmers;

// public class 마지막 두 원소 {
  
// }

// 출처:프로그래머스
// https://school.programmers.co.kr/learn/courses/30/lessons/181927

//풀이 과정

/*
 * class Solution {
    public int[] solution(int[] num_list) {
        if(num_list[num_list.length-1] > num_list[num_list.length-2]){
            int[] result = new int[num_list.length+1];
            for(int i =0; i<num_list.length; i++){
                result[i] = num_list[i];
            }
            result[result.length-1] = num_list[num_list.length-1] - num_list[num_list.length-2];
            return result;
        }
        else{
            int[] result = new int[num_list.length+1];
            for(int i =0; i<num_list.length; i++){
                result[i] = num_list[i];
            }
            result[result.length-1] = num_list[num_list.length-1]*2;
            return result;
        }
    }
}
 */