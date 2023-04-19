# sort가 알파벳 순서대로도 정렬해준다! 개념

# 풀이1

def solution(my_string):
    a=my_string.lower()
    b=list(a)
    answer = "".join(b)
    return answer

# 풀이2

def solution(my_string):
    return "".join(sorted(my_string.lower()))

