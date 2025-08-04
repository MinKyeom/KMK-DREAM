// package Programmers;

// public class 배열 만들기4 {
  
// }

//출처:프로그래머스,
//https://school.programmers.co.kr/learn/courses/30/lessons/181918

/*
 * // list 정의
import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> result = new ArrayList<>();
        int i = 0;
        while(i<arr.length){
            if(result.size()==0){
                result.add(arr[i]);
                i++;
            }
            else{
                if( result.get(result.size()-1) <arr[i]){
                    result.add(arr[i]);
                    i++;
                }
                else{
                    result.remove(result.size()-1);
                }
            }
            // System.out.println(result);
        }
        // System.out.print(result);
        int[] stk = new int[result.size()];
        for(int k =0; k<result.size(); k++){
            stk[k]=result.get(k);
        }
        
        return stk;
    }
}
 */