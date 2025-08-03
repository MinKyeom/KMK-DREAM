// package Programmers;

// public class 콜라츠 수열 만들기 {
  
// }


// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181919


/*
 * import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> check = new ArrayList<>();
        while(n!=1){
            check.add(n);
            if(n%2==0){
            n=n/2;
            }
            else{
            n= (n*3+1);
            }
        }
        check.add(n);
        
        int[] answer = new int[check.size()];
        
        int k = 0;
        for(int num:check){
            answer[k]=num;
            k++;
        }
        return answer;
    }
}
 */