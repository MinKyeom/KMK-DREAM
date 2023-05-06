# 풀이1 치킨 쿠폰
def solution(chicken):
    result=0
    x=int(chicken/10)
    result+=x
    y=(chicken%10)+x
    result+=int(y/10)
    z=(y%10)+int(y/10)
    # result+=int(z/10)
    # print(result)
    if z>=10:
        while True:
            if z>=10:
                y=int(z/10)
                result+=y
                z=int(z/10)+(z%10)
                print(z)
            else:break
    return result

# 풀이2

def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer