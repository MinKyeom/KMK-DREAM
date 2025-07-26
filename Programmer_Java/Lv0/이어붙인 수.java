// package Programmers;

// public @interface 이어붙인 수 {
  
// }

// 출처:프로그래머스,
//https://school.programmers.co.kr/learn/courses/30/lessons/181928

//풀이과정
/*
 * class Solution {
    public int solution(int[] num_list) {
        String a = "";
        String b = "";
        int num_length = num_list.length;
        for(int i = 0; i < num_length; i++){
            // 홀수인 경우
            if(num_list[i]%2 ==1){
                String fir = Integer.toString(num_list[i]);
                a+=fir;
            }
            else{
                String sec =Integer.toString(num_list[i]);
                b+=sec;
            }
        }
        int result = Integer.parseInt(a)+ Integer.parseInt(b);
        return result;
    }
}
 */