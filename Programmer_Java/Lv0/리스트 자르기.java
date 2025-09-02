// package Programmers;

// public class 리스트 자르기 {
  
// }

// 출처:프로그래머스,
// https://school.programmers.co.kr/learn/courses/30/lessons/181897

// 풀이과정 

/*
 * class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        
        if(n==1){
            int[] answer = new int[b+1];
            for(int k =0; k<=b; k++){
                answer[k] = num_list[k];
            }
            return answer;
        }
        
        else if(n==2){
            int[] answer = new int[num_list.length-a];
            for(int k =a; k<num_list.length; k++){
                answer[k-a] = num_list[k];
            }
            return answer;
        }
        
        else if(n==3){
            int[] answer = new int[b-a+1];
                for(int k =a; k<=b; k++){
                    answer[k-a] = num_list[k];
                }   
            return answer;
            }
        
        else{
            int index_num = 0;
            for(int k=a; k<=b; k+=c){
                    index_num++;
                }
            
            int[] answer = new int[index_num];
            int count = 0;    
                for(int k=a; k<=b; k+=c){
                    answer[count] = num_list[k];
                    count++;
                }
            return answer;
            }
    }
}
      

 */

// 풀이 과정_개선 중 
/*
 * class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        
        if(n==1){
            int[] answer = new int[b];
            for(int k =0; k<=b; k++){
                answer[k] = num_list[k];
            }
            return answer;
        }
        
        else if(n==2){
            int[] answer = new int[num_list.length-a+1];
            for(int k =a; k<num_list.length; k++){
                answer[k-a] = num_list[k];
            }
            return answer;
        }
        
        else if(n==3){
            int[] answer = new int[b-a+1];
                for(int k =a; k<=b; k++){
                    answer[k-a] = num_list[k];
                }   
            return answer;
            }
        
        else{
            int index_num = (int) (b-a+1)/c +1;

            int[] answer = new int[index_num];
            int count = 0;    
                for(int k=a; k<=b; k+=c){
                    answer[count] = num_list[k];
                    count++;
                }
            return answer;
            }
    }
}
      
 */

// 풀이과정_개선 중

/*
 * class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        
        if(n==1){
            int[] answer = new int[b];
            for(int k =0; k<b; k++){
                answer[k] = num_list[k];
            }
            return answer;
        }
        else if(n==2){
            int[] answer = new int[num_list.length-a];
            for(int k =a; k<num_list.length; k++){
                answer[k] = num_list[k];
            }
            return answer;
        }
        else if(n==3){
            if(a>=b){
            int[] answer = new int[a-b+1];
                for(int k =a; k>=b; k--){
                answer[a-k] = num_list[k];
            }   
            return answer;
        }
            else{
            int[] answer = new int[b-a+1];
                for(int k =a; k<b; k++){
                answer[k-a] = num_list[k];
            }   
            return answer;
            }
        else{
            if(a>=b){
            int[] answer = new int[b-a+1];
            for(int k=a; k>=b; k-=c ){
                answer[a-k] = num_list[k];
                }
            }
            return answer;
            else{
            for(int k=a; k<b; k+=c){
                answer[k-a] = num_list[k];
            }
                return answer
            }
        }

        
    }
}
 */