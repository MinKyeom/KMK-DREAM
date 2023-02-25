"""
내 풀이 오답

N,K=map(int,input().split())
list_use=list(input().split())
list_con=[]
#처음에는 for문에 넣어서 하나씩 입력받은걸 리스트에 넣으려고 했음!

count=0
for x in list_use:
        if len(list_con)>=N:
            if x in list_con:
                continue
            else:
                list_con.pop()
                list_con.append(x)
                count +=1
        else:
            if x in list_con:
                continue
            else:
                list_con.append(x)
print(count)
"""





