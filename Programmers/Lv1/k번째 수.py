# 내 풀이
def solution(array, commands):
    result=[]
    for x,y,z in commands:
        k=array[x-1:y]
        k.sort()
        r=k[z-1]
        result.append(r)
    return result

# 다른 사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
