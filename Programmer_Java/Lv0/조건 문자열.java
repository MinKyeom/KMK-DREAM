// package Programmers;

// public class 조건 문자열 {
  
// }

// 출처: 프로그래머스
//https://school.programmers.co.kr/learn/courses/30/lessons/181934
// 풀이 과정
// eq,ineq 조합 한 후 <,= 구현을 if문으로 구분하고나서 구하기
/* 
class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if(eq.equals("=") && ineq.equals(">")){
            System.out.print("1");
            if ( n >= m){
                return 1;
            }
            else {
                return 0;
            }
        }
        else if(eq.equals("=") && ineq.equals("<")){
            System.out.print("2");
            if (n<=m){
                return 1;
            }
            else{
                return 0;
            }
        }
        else if (eq.equals("!") && ineq.equals(">")){
            System.out.print("3");
            if (n>m){
                return 1;
            }
            else{
                return 0;
            }
        }
        else{
            System.out.print("4");
            if(n<m) {
                return 1;
            }
            
            else {
                return 0;
            }
        }
    }
}
*/


// 풀이 과정 개선 중 
/*
 * // eq,ineq 조합 한 후 <,= 구현을 if문으로 구분하고나서 구하기

class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        if(eq=="=" && ineq == ">"){
            if ( n >= m){
                return 1;
            }
            else{
                return 0;
            }
        elseif(eq=="=" && ineq=="<"){
            if (n<=m){
                return 1;
            }
            else{
                return 0;
            }
        elseif (eq=="!" && ineq==">"){
            if (n>m){
                return 1;
            }
            else{
                return 0;
            }
        else {
            if(n<m){
                return 1;
            }
            else{
                return 0;
            }
        }
        }
        }
            }
        }
    }
}
 * 
 */
