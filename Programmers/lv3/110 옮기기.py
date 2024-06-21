"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/77886
"""
# 내 풀이(개선 중)
"""
조건:0과 1로 이루어진 x를 바탕으로 주어진 s를 순서를 바꿔 최소값을 return 

생각방향: 110을 지속적으로 찾아내기
원래 s에 있는 형태의 110이 아니더라도 중간에 변형에 의하여 생긴 110 또한 존재
110 빼서 111 자리 앞에 넣어줘야한다

# 필요한 생각: 지속적으로 반복되는 110대한 처리 생각 


"""
# sol3
from collections import deque


def solution(s):
    result = []

    # 하나씩 추출
    for i in s:

        # 반복 방지
        start = 0

        # 형태 변환
        i = list(i)
        while True:
            i = list(i)

            # 루프 나올지 여부
            flag = False

            for a in range(start, len(i) - 2):
                if i[a] + i[a + 1] + i[a + 2] == "110":
                    k = a
                    break

            # 110이 없을 때
            else:
                result.append("".join(i))
                break

            del i[k]
            del i[k]
            del i[k]

            check = []

            # 재배열
            for b in range(len(i) - 2):
                if i[b] + i[b + 1] + i[b + 2] == "111":
                    n = b
                    start = b + 3
                    break


            else:
                if i[-1] == "0":
                    final = i + list("110")
                    result.append("".join(final))
                    break

                else:
                    for f in range(len(i) - 1, -1, -1):
                        if i[f] == "0":
                            final = i[:f + 1] + list("110") + i[f + 1:]
                            result.append("".join(final))
                            break
                    else:
                        final = list("110") + i
                        result.append("".join(final))
                        break

                    break

            i = i[:n] + list("110") + i[n:]

    return result


"""
# sol2
from collections import deque

def solution(s):
    result=[]

    for i in s:
        i=deque(list(i))

        start=[]

        while len(start)<len(i) or i:
            k=i.popleft()
            start.append(k)

            if len(start)>=3:
                if start[len(start)-3]+start[len(start)-2]+start[len(start)-1]=="111":

                    start.pop()
                    start.pop()
                    start.pop()

                    i= deque(list("111")+list(i))
                    print(i,"i 재배열 전 ")
                    # 110 찾아 재배열 
                    one=[]
                    while i:
                        t=i.popleft()
                        one.append(t)

                        if len(one)<3:
                            continue
                        else:
                            if one[len(one)-3]+one[len(one)-2]+one[len(one)-1]=="110":
                                one.pop()
                                one.pop()
                                one.pop()

                                check=[]
                                start+=one
                                check+=list("110")
                                check+=list(i)
                                i=deque(check)
                                break
                    else:
                        start+=one

                    print(start,i,"재배열 후")
    return result
"""

# sol1
"""
from collections import deque 

def change_s(i,j):
    #111 뒤에 있는 110 찾기
    r=len(i)

    start=i[:]

    i=deque(list(i))

    for k in range(j,r-2):
        if i[k]+i[k+1]+i[k+2]=="110":
            del i[k]
            del i[k]
            del i[k]
            break
    else:
        return start,True

    i=list(i)

    start=i[:j]
    end=i[j:]

    return "".join(start)+"110"+"".join(end),False    


def solution(s):
    result=[]

    for i in s:

        #111 찾기

        for j in range(len(i)-2):
            if i[j]+i[j+1]+i[j+2]=="111":
                i,flag=change_s(i,j)

                if flag==True:
                    result.append(i)
                    break
        else:
            result.append(i)


    return result 
"""

# 내 풀이(개선 중)
"""
조건:0과 1로 이루어진 x를 바탕으로 주어진 s를 순서를 바꿔 최소값을 return 

생각방향: 110을 지속적으로 찾아내기
원래 s에 있는 형태의 110이 아니더라도 중간에 변형에 의하여 생긴 110 또한 존재
110 빼서 111 자리 앞에 넣어줘야한다 

"""
# sol2
from collections import deque


def solution(s):
    result = []

    for i in s:
        i = deque(list(i))

        start = []

        while len(start) < len(i) or i:
            k = i.popleft()
            start.append(k)

            if len(start) >= 3:
                if start[len(start) - 3] + start[len(start) - 2] + start[len(start) - 1] == "111":

                    start.pop()
                    start.pop()
                    start.pop()

                    i = deque(list("111") + list(i))
                    print(i, "i 재배열 전 ")
                    # 110 찾아 재배열
                    one = []
                    while i:
                        t = i.popleft()

                        one.append(t)

                        if len(one) < 3:
                            continue
                        else:
                            if one[len(one) - 3] + one[len(one) - 2] + one[len(one) - 1] == "110":
                                one.pop()
                                one.pop()
                                one.pop()

                                check = []
                                start += one
                                check += list("110")
                                check += list(i)
                                i = deque(check)
                                break
                    else:
                        start += one

                    print(start, i, "재배열 후")
    return result


# sol1
"""
from collections import deque 

def change_s(i,j):
    #111 뒤에 있는 110 찾기
    r=len(i)

    start=i[:]

    i=deque(list(i))

    for k in range(j,r-2):
        if i[k]+i[k+1]+i[k+2]=="110":
            del i[k]
            del i[k]
            del i[k]
            break
    else:
        return start,True

    i=list(i)

    start=i[:j]
    end=i[j:]

    return "".join(start)+"110"+"".join(end),False    

def solution(s):
    result=[]

    for i in s:

        #111 찾기

        for j in range(len(i)-2):
            if i[j]+i[j+1]+i[j+2]=="111":
                i,flag=change_s(i,j)

                if flag==True:
                    result.append(i)
                    break
        else:
            result.append(i)


    return result 
"""
# 내 풀이(개선 중)
"""
조건:0과 1로 이루어진 x를 바탕으로 주어진 s를 순서를 바꿔 최소값을 return 

생각방향: 110을 지속적으로 찾아내기
원래 s에 있는 형태의 110이 아니더라도 중간에 변형에 의하여 생긴 110 또한 존재

"""
from collections import deque


def solution(s):
    result = []

    check = []

    for i in s:
        i = i.replace("110", "x")
        print(i)
        num = i.count("x")
        print(num)

    return result

# 다른 사람 풀이
def solution(s):
    answer = []
    for string in s:
        count, idx, stack = 0, 0, ""
        while idx < len(string):            # 110 찾기
            if string[idx] == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                count += 1
            else:
                stack += string[idx]
            idx += 1

        idx = stack.find("111")             # 110이 빠진 string에서 111 찾기
        if idx == -1:                       # 0뒤에 110 반복해 붙이기
            idx = stack.rfind('0')
            stack = stack[:idx+1]+"110"*count+stack[idx+1:]
        else:                               # 111앞에 110 반복해 붙이기
            stack = stack[:idx]+"110"*count+stack[idx:]
        answer.append(stack)
    return answer

# 110 다 추출하고 111앞에 넣기
def solution(s):
    answer = []

    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            # 110이 나온 경우
            if(len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0'):
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)

        # 110을 모두 제거했으므로 남은 문자열에서 연속된 1이 존재하는 곳은 한 곳밖에 없다.
        count_1 = 0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                count_1 += 1
        answer.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return answer