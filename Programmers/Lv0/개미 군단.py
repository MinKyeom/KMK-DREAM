# 내 풀이
def solution(hp):
    count=0
    while True:
        for a in [5,3,1]:
            if hp>=a:
                count+=int(hp/a)
                hp=hp%a
                if hp==0:
                    return count
            if hp==0:
                return 0


# 다른 사람 풀이
def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)