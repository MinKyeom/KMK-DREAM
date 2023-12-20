# 내 풀이
def solution(n, t, m, p):
    from collections import deque
    check = m * t
    all_num = deque([0])
    count = 1

    while True:
        start = count
        num = deque([])

        while True:
            start, j = divmod(start, n)  # i 몫 j 나머지

            if start == 0:
                if j != 0:
                    if j == 10:
                        num.appendleft("A")
                    elif j == 11:
                        num.appendleft("B")
                    elif j == 12:
                        num.appendleft("C")
                    elif j == 13:
                        num.appendleft("D")
                    elif j == 14:
                        num.appendleft("E")
                    elif j == 15:
                        num.appendleft("F")
                    else:
                        num.appendleft(j)
                break
            else:
                if j == 10:
                    num.appendleft("A")
                elif j == 11:
                    num.appendleft("B")
                elif j == 12:
                    num.appendleft("C")
                elif j == 13:
                    num.appendleft("D")
                elif j == 14:
                    num.appendleft("E")
                elif j == 15:
                    num.appendleft("F")
                else:
                    num.appendleft(j)
        all_num += num
        if len(all_num) >= check:
            break

        count += 1

    all_num = "".join(list(map(str, list(all_num)[p - 1::m][0:t])))

    return all_num

# 다른 사람 풀이
big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer