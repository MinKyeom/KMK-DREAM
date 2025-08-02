//출처:프로그래머스
//https://school.programmers.co.kr/learn/courses/30/lessons/181921

/*
 * 
 * /*
범위의 숫자를 for문을 만든 후 
해당 숫자를 string으로 변경 후 
split 후 각 숫자에 대하여 0,5 진단
그리고 맞으면 append

// 부족한 개념: 객체 타입 정의도 확인해보기,다이아몬드 연산자, 생성자 호출

import java.util.*; // *:라이브러리 내 모든 거 가져오기
class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> check = new ArrayList<>();
        
        for(int i=l; i<=r; i++){
            // 쪼개기 위해 한 정수 문자로 변환
            String num = String.valueOf(i);
            // 변환한 문자를 한 문자씩 분리(5,0만 있는 지 확인 위해서)
            String[] num_split = num.split("");
            //new HashSet<>(Arrays.asList(arr));
            // set으로 바꾼 후 중복 제거
            Set<String> num_set = new HashSet<>(Arrays.asList(num_split));
            // 예시 조건
            Set<String> case1 = new HashSet<>(Arrays.asList("5"));
            Set<String> case2 = new HashSet<>(Arrays.asList("0"));
            Set<String> case3 = new HashSet<>(Arrays.asList("0","5"));
            if(num_set.equals(case1) || num_set.equals(case2) || num_set.equals(case3) ){
                check.add(i);
        }
        
    }
    // 자바 조건에 따라 리스트 배열로 바꾸기
    int[] result = new int[check.size()];
    for(int t = 0; t < check.size(); t++ ){
        result[t] = check.get(t);
    }
    if(result.length == 0){
        return new int[]{-1};
    }
    else{
        return result;
    }

}
}
 */