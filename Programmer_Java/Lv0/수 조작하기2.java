// package Programmers;

// public class 수 조작하기2 {
  
// }
//출처:프로그래머스,
//https://school.programmers.co.kr/learn/courses/30/lessons/181925

//풀이 과정
/* 
class Solution {
    public String solution(int[] numLog) {
        String result = "";
        for(int i = 1; i<numLog.length; i++){
            if( numLog[i]-numLog[i-1] == 1){
                result+="w";
            }
            else if(numLog[i]-numLog[i-1]==-1){
                result+="s";
            }
            else if(numLog[i]-numLog[i-1]==10){
                result+="d";
            }
            else if(numLog[i]-numLog[i-1]==-10){
                result+="a";
            }
        }
        return result;
    }
}
*/