// package Programmers;

// public class 수열과 구간쿼리4 {
  
// }

//출처:프로그래머스
//https://school.programmers.co.kr/learn/courses/30/lessons/181922

/*
 * // 원래 원본 arr 그래도 지키는 게 좋은 코드라는 걸 명심하자!
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        for(int[] check:queries){
            int s = check[0];
            int e = check[1];
            int k = check[2];
            
            for(int i =s; i<=e; i++ ){
                if(i%k==0){
                    arr[i]=arr[i]+1;
                }
            }
        }
        return arr;
    }
}
 */