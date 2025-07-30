// package Programmers;

// public class 수열과 구간쿼리2 {
  
// }

//출처:프로그래머스,
//https://school.programmers.co.kr/learn/courses/30/lessons/181923

/*
 * class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] result = new int[queries.length];
        int count = 0;
        for(int[] array_num:queries){
           int s=array_num[0];
           int e=array_num[1];
           int k=array_num[2];
           int start = k;
           int change = 0;
           for(int i=s; i<=e; i++){
               if(arr[i]>k && start<arr[i] && change==0 ){
                   start = arr[i];
                   change = 1;
               }
               else if(arr[i]>k && start>arr[i] && change!=0 ){
                   start = arr[i];
               }
           }
           if(start==k){
             result[count]=-1;
             count++;
             }
           else{
             result[count]=start;
             count++;
             }
        }
        

        return result;
    }
}
 */
