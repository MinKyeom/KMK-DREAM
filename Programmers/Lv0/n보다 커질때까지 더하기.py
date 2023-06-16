# 내 풀이
def solution(numbers, n):
    count=0
    for x in numbers:
        count+=x
        if count>n:
            return count
# 다른 사람 풀이
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)