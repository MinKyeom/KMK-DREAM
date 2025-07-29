// package Programmers;

// public class 수 조작하기 {
  
// }

//출처:프로그래머스
//https://school.programmers.co.kr/learn/courses/30/lessons/181926
// 풀이과정
/* 
class Solution {
    public int solution(int n, String control) {
        char[] check = control.toCharArray();
        for(int i=0; i<check.length; i++){
            if(check[i]=='w'){
                n+=1;
            }
            else if(check[i]=='s'){
                n-=1;
            }
            else if(check[i]=='d'){
                n+=10;
            }
            else if(check[i]=='a'){
                n-=10;
            }
        }
        
        return n;
    }
}
*/

// 풀이과정 개선중
/* 
class Solution {
    public int solution(int n, String control) {
        char[] check = n.toCharArray();
        for(int i=0; i<check.length; i++){
            if(check[i]=='w'){
                n+=1;
            }
            else if(check[i]=='s'){
                n-=1;
            }
            else if(check[i]=='d'){
                n+=10;
            }
            else if(checl[i]=='a'){
                n-=10;
            }
        }
        
        return n;
    }
}
*/