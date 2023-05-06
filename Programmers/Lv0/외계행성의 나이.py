# 내 풀이
def solution(age):
    x=str(age)
    english=["a","b","c","d","e","f","g","h","i","j"]
    for k in range(10):
        x=x.replace(str(k),english[k])
    answer = x
    return answer

# 다른 사람 풀이
def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])

