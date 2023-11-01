# 내 풀이
def solution(s):
    from collections import deque
    result = 0

    count = 0

    k = deque(list(s))

    check = []

    open_ = ["[", "(", "{"]

    close_ = ["]", ")", "}"]

    if len(s) == 1:
        return 0

    while count < len(s):

        if k[-1] in open_ or k[0] in close_:
            a = k.popleft()
            k.append(a)
            count += 1


        else:
            check = []
            flag = False
            for b in k:
                if b in open_:
                    check.append(b)

                elif b in close_:
                    if len(check) == 0:
                        flag = True
                        break

                    else:
                        c = close_.index(b)
                        d = open_.index(check[-1])

                        if c == d:
                            check.pop()

                        else:
                            break

            if len(check) == 0:
                if flag == False:
                    result += 1
                a = k.popleft()
                k.append(a)
                count += 1

            else:
                a = k.popleft()
                k.append(a)
                count += 1

    return result

# 다른 사람 풀이
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer