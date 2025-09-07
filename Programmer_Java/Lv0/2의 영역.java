// package Programmers;

// public class 2의 영역 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181894

// 풀이과정 
/*
 * // 2 들어가 있는 리스트를 만든 후 
// 2가 나오긴 전까지 들어갈 리스트를 만든 후 2가 나오면 최종적으로 합쳐주는 방식

import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        List<Integer> before = new ArrayList<>();
        List<Integer> after = new ArrayList<>();
        for(int i =0; i < arr.length; i++){
            if(arr[i]==2){
                after.addAll(before);
                after.add(arr[i]);
                before.clear();
            
            }
            else{
                if(after.size() >= 1){
                    before.add(arr[i]);
                }
            }
        }
        // System.out.println(after);
        
        int[] answer = new int[after.size()]; 
        
        for(int t =0 ; t<after.size(); t++){
            answer[t] = after.get(t);
            
        }
        if(after.size()==0){
            return new int[] { -1 };
        }
        
        else{
            return answer;
        }
        
    
    }

}
 */

/*
 * // 2 들어가 있는 리스트를 만든 후 
// 2가 나오긴 전까지 들어갈 리스트를 만든 후 2가 나오면 최종적으로 합쳐주는 방식

import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        List<Integer> before = new ArrayList<>();
        List<Integer> after = new ArrayList<>();
        for(int i:arr){
            
        }
        return answer;
        
    }

}
 */