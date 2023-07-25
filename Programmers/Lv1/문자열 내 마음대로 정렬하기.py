# 내 풀이
def solution(strings, n):
    check = []
    for x in strings:
        k = x[n:n + 1]
        check.append([k, x])

    check.sort()

    result = []

    for y, z in check:
        result.append(z)

    return result

# 다른 사람 풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])
strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))