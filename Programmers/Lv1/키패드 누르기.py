# 내 풀이
def solution(numbers, hand):
    l = "*"
    r = "#"
    num = "123456789*0#"
    middle = "2580"
    result = []
    for x in numbers:
        if x == 3 or x == 6 or x == 9:
            result.append("R")
            r = x
        elif x == 1 or x == 4 or x == 7:
            result.append("L")
            l = x
        else:
            d_r = 0
            d_l = 0
            if str(r) in middle:
                d_r = abs(middle.find(str(x)) - middle.find(str(r)))
            if str(l) in middle:
                d_l = abs(middle.find(str(x)) - middle.find(str(l)))
            if not str(r) in middle:
                a = num.find(str(r))
                a = num[a - 1:a]
                d_r = abs(middle.find(str(x)) - middle.find(str(a))) + 1
            if not str(l) in middle:
                b = num.find(str(l))
                b = num[b + 1:b + 2]
                d_l = abs(middle.find(str(x)) - middle.find(str(b))) + 1
            if d_r < d_l:
                r = x
                result.append("R")
            elif d_l < d_r:
                l = x
                result.append("L")

            elif d_r == d_l:
                if hand == "right":
                    r = x
                    result.append("R")
                else:
                    l = x
                    result.append("L")

    return "".join(result)

# 다른 사람 풀이
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
