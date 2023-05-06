# 풀이 1

def solution(cipher, code):
    answer = ''
    z=[]
    for x in range(1,len(cipher)+1):
        if x%code==0:
            y=cipher[x-1]
            z.append(y)
    answer="".join(z)
    return answer

# 다른 사람 풀이

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer