# 내 풀이
def solution(a, b):
    # 1:31 2:28 3:31 4:30 5:31 6:30 7:31 8:31 9:30 10:31 11:30 12:31
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    if a > 1:
        for x in range(a - 1):
            if a > 1:
                count += day[x]
        print(count)
        count += b
    else:
        count += b

    result = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    k = count % 7
    print(count)

    return result[k]

# 다른 사람 풀이
def getDayName(a,b):
    answer = ""
    if a>=2:
        b+=31
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30#4월
                    if a>=6:
                        b+=31#5월
                        if a>=7:
                            b+=30#6월
                            if a>=8:
                                b+=31#7월
                                if a>=9:
                                    b+=31#8월
                                    if a>=10:
                                        b+=30#9월
                                        if a>=11:
                                            b+=31#10월
                                            if a==12:
                                                b+=30#11월
    b=b%7

    if b==1:answer="FRI"
    elif b==2:answer="SAT"
    elif b==3:answer="SUN"
    elif b==4:answer="MON"
    elif b==5:answer="TUE"
    elif b==6:answer="WED"
    else:answer="THU"
    return answer


print(getDayName(5,24))