// 출처:프로그래머스
// https://school.programmers.co.kr/learn/courses/30/lessons/181939

class Solution {
    public int solution(int a, int b) {
        String c=String.valueOf(a);
        String d=String.valueOf(b);    
        if(Integer.parseInt(c+d) >Integer.parseInt(d+c)){
        return (Integer.parseInt(c+d));
        }
        
        else{
             return (Integer.parseInt(d+c));  
        }
    }
}