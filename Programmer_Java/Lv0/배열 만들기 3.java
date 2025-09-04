// package Programmers;
// public class 배열 만들기 3 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181895

// 풀이과정 

/*
 * import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> num_list = new ArrayList<>();
        
        for(int i = 0; i< intervals.length; i++ ){
            int start = intervals[i][0];
            int end = intervals[i][1];
            
            for(int k = start; k<=end; k++){
                num_list.add(arr[k]);
            }
        
        }
        // for(int t = 0; t<num_list.size(); t++){
        //     System.out.println(num_list.get(t));
        // }
        
        int[] answer = new int[num_list.size()];
        
        for(int num = 0; num<num_list.size(); num++){
            answer[num] = num_list.get(num);
        }
        return answer;
    }
}
 */