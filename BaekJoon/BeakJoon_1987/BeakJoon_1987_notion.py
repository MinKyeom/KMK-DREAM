x=2
y=3

def test(x,y):
    x +=1
    y +=1
    return x,y # 3,4
#경우의 수
# x,y=test(x,y) #x,y 변경 x' y'

#경우의 수 2
x=test(x,y) # x에 (x,y)가 전달된다! 둘다 받고 싶다면 위의 경우의 수처럼

print(x,y) #