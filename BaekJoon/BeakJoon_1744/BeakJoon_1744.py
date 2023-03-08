
N=int(input())
num=[]
num_plus=[]
num_minus=[]
count_plus=0
count_minus=0
num_1=[]

for a in range(N):
    x=int(input())
    num.append(x)
    if num[a]>1:
        num_plus.append(num[a])
    elif num[a]<=0:
        num_minus.append(num[a])
    elif num[a]==1:
        num_1.append(num[a])

if len(num_plus)%2==0:
    b=sorted(num_plus)
    b.reverse()
    for c in range(0,len(b),2):
        count_plus+=b[c]*b[c+1]

else:
    b = sorted(num_plus)
    b.reverse()
    for c in range(0,len(b)-1,2):
        count_plus+=b[c]*b[c+1]
    count_plus+=b[len(b)-1]

if len(num_minus)%2==0:
    d=sorted(num_minus)
    for e in range(0,len(d),2):
        count_minus+=d[e]*d[e+1]

else:
    d=sorted(num_minus)
    for e in range(0,len(d)-1,2):
        count_minus+=d[e]*d[e+1]
    count_minus+=d[len(d)-1]

print(count_plus+count_minus+len(num_1))


#출력 결과 또한 정답!!!!