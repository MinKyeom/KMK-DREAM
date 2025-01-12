"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/250121
"""

# 풀이과정
def solution(data, ext, val_ext, sort_by):

    sort_check=["code","date","maximum","remain"]

    check=[]

    # 최솟값 뽑을 데이터
    check_data=sort_check.index(ext)

    # 나열할 기준 데이터
    check_sort=sort_check.index(sort_by)

    for i in data:
        if i[check_data] < val_ext:
            check.append(i)


    result=sorted(check, key=lambda x:x[check_sort])

    return result

# 다른 사람 풀이
def solution(data, ext, val_ext, sort_by):
    answer = []
    by = [ "code", "date", "maximum", "remain" ]

    for item in data:
        if item[by.index(ext)] < val_ext:
            answer.append(item)

    return sorted(answer, key=lambda x: x[by.index(sort_by)])
