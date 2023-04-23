#풀이 1
def solution(score):
    result = []
    ave = []
    for a, b in score:
        x = (a + b) / 2
        ave.append(x)
    for c in ave:
        count = 1
        for d in ave:
            if c < d:
                count += 1
            else:
                continue
        result.append(count)
    return result

#풀이 2

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]