# 내 풀이(개선 중)
def solution(numbers):
    result = []
    for a in numbers:
        k = list(str(bin(a))[2:])
        k_1 = bin(a)  #
        t = a + 1
        print(type(k_1))

        #         while True:
        #             c=bin(t)
        #             d=c-k_1
        #             e=str(d)[2:]
        #             if e.count("1")<=1:
        #                 result.append(t)
        #                 break
        #             else:
        #                 t+=1

        """
        while True:
            b=list(str(bin(t))[2:])
            c=len(b)-len(k)
            e=["0"]*c+k

            count=0

            for f in range(len(e)-1,-1,-1):
                if b[f]!=e[f]:
                    count+=1
                    if count>2:
                        break

            if count<=2:
                result.append(t)
                break

            else:
                t+=1
            """

    return result
