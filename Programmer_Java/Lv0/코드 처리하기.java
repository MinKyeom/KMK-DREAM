// package Programmers;

// public class 코드 처리하기 {
  
// }

// 출처: 프로그래머스
// https://school.programmers.co.kr/learn/courses/30/lessons/181932

// 풀이과정_ 개선 중 
/*
 * class Solution {
    public String solution(String code) {
        // 시작 할 떄 모드 
        int mode = 0;
        int num = code.length();
        String result = "";
        for(int i=0; i < num; i++){
            if(code.charAt(i)=='1'){
                if(mode==1){
                    mode = 0;
                }
                else{
                    mode = 1; 
                }
            }
            
            else{
                if(mode==0){
                    if(i%2==0){
                        result+=code.charAt(i);
                    }
                }
                else{
                    if(i%2==1){
                        result+=code.charAt(i);
                    }
                }
            }
        }
        String answer = "";
        return result;
    }
}
 */