"""
dfs를 활용하는 생각이 매끄럽게 이루어지지 못하며,
공백 제거 등의 아이디어의 정확성 부족

dfs 약점 보완하기!

기업 코테 중 dfs 안쪽으로 깊게 사고 후 맨 아래 부터 위로 올리는 사고 과정 생각해보기!!!

"""

from collections import deque

check="a(b(c(d)c)b)a"

check=list(check)

check=deque(check)

def make():
    global check

    s=""

    while True:
        k=check.popleft()

        if k=="(":
            s+=make()

        elif k==")":
            break

        else:
            s+=k

    return s*2

def start():
    global check

    result=""

    while check:
        k=check.popleft()

        if k=="(":
            result+=make()

        elif k!=")":
            result+=k

    return result

print(start())