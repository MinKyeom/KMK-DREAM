// package Programmers;

// public class 배열 조작하기 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181893

// 풀이 과정
/*
 * import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        
        Deque<Integer> check = new ArrayDeque<>();
        
        for(int c: arr){
            check.addLast(c);
        }
        
        for(int q = 0 ; q < query.length; q++){
            
            if(q%2==0){
                int start_length = check.size();
                for(int start = query[q]+1; start<start_length; start++){
                    check.removeLast();
                }
            
            }
            
            else{
                for(int start = query[q]-1; start >= 0; start--){
                    check.removeFirst();
                }
            }
        }
        
        // deque > List변환
        List<Integer> change_check = new ArrayList<>(check);
        
        int[] answer = new int[check.size()];
            
        for(int t = 0; t<change_check.size(); t++){
            answer[t] = change_check.get(t);
        }
        
        return answer;
    }
}
 */

// 풀이과정_개선 중

/*
 * import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        
        Deque<Integer> check = new ArrayDeque<>();
        
        for(int c: arr){
            check.addLast(c);
        }
        
        for(int q = 0 ; q < query.length; q++){
            if(q%2==0){
                for(int start = query[q]+1; start<check.size(); start++){
                    check.removeLast();
                }
            
            }
            else{
                for(int start = query[q]-1; start>=0; start--){
                    check.removeFirst();
                }
            }
        }
        
        // deque > List변환
        List<Integer> change_check = new ArrayList<>(check);
        
        int[] answer = new int[check.size()];
            
        for(int t = 0; t<change_check.size(); t++){
            answer[t] = change_check.get(t);
        }
        
        return answer;
    }
}
 */

// 풀이과정_개선 중 

/*
 * import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = {};
        
        List<Integer> check = new ArrayList<>();
        
        for(int c: arr){
            check.add(c);
        }
        
        for(int a = 0 ; a< arr.length; a++){
            if(a%2==0){
                
                for(int q: query){
            
                    for(int i = 0; i < check.size();){
                
            }
        }
            }
            else{
                
                for(int q: query){

                    for(int i = 0; i < check.size();){
                
            }
        }
            }
        }
        

        
        return answer;
    }
}
 */