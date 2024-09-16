"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42893
"""

# 내 풀이(개선 중)
"""
조건:
기본점수: 검색어가 등장하는 횟수
외부링크 수:다른 외부 페이지와 연결된 개수 
링크점수:기본점수/외부링크 수 총합
"""

def solution(word, pages):
    new = []
    word = word.upper()

    for p in pages:
        n = p.upper()

        new.append(n)

    check = [[0] * 3 for i in range(len(new))]

    for n in range(len(new)):
        check[n][1] = new[n].count("<A HREF")

        l = new[n].split(" ")

        for f in l:
            if f == word:
                check[n][0] += 1

    answer = 0
    return answer