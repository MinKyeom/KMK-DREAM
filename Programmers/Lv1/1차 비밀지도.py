# 내 풀이
def solution(n, arr1, arr2):
    p = n
    for x in range(n):
        arr1[x] = bin(arr1[x])
        arr1[x] = str(arr1[x])[2:]
        arr2[x] = bin(arr2[x])
        arr2[x] = str(arr2[x])[2:]
        a_1 = p - len(arr1[x])
        a_2 = p - len(arr2[x])
        v = ["0" for c in range(a_1)]
        w = ["0" for d in range(a_2)]
        v = "".join(v)
        w = "".join(w)
        arr1[x] = v + str(arr1[x])
        arr2[x] = w + str(arr2[x])
    print(arr1)
    print(arr2)
    result = []

    for y in range(n):
        k = []
        a = list(arr1[y])
        b = list(arr2[y])
        for z in range(len(a)):
            if a[z] == "1" or b[z] == "1":
                k.append("#")
            else:
                k.append(" ")
        l = "".join(k)
        result.append(l)

    print(result)

    return result

# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
