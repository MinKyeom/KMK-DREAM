# a=[(1,2),(2,3)]
#
# for x,y in a:
#     print(x)
#     print(y)
#     print()


# a=[(1,2)]
#
# print(len(a))
# a=[]
# for x in range(2):
#     a.append(list(map(int,input().split())))
#
#
# print(a)
# print(sum(a))

# a=[(1,2),(2,3)]
#
# print(bool(1 in a))
#
# print(bool((1,2) in a))
#
# print(len(a))
#
# b=[]
#
# print(len(b))

# a=[(1,2),(2,3)]
#
# for x,y in a:
#     print(x)
#     print(y)
#     print()

# list_ma=[250,200,130,150,100,60]
#
# count=0
#
# for x in list_ma:
#     count += x
#
# print(count)
# list=[]

# def fuction(x,y):
#    new_x=x+1
#    new_y=y+1
#    x=new_x
#    y=new_y
#    print(x,y)
#
# a=[(1,2),(3,2)]
#
# for c,d in a:
#     fuction(c,d)
#
# print(a)
    #print(c,d) # 1 2 # 3 2 출력

# for c,d in a:
#     fuction(c,d)


# list_map=[180,200,130,50,50,150,50]
#
# count=0
#
# for x in list_map:
#    count += x
#
# print(count)


# def test(x,y):
#     x +=1
#     y +=1
#     print(x,y)
#     return x,y

x,y=1,2

def test(x,y):
    global new_x,new_y
    new_x =x+1
    new_y =y+1
    print(x,y)
    return new_x,new_y


def test_2(c,d):
    global c,d
    c =c+1
    d =d+1
    return c,d

print(x)
print()
print(y)
print("------")
print()
print("---함수 실행 전---")
print("실험")
test(x,y)
print("---함수 실행 후---")
print(new_x)
print()
print(new_y)
print("--------")
v=1
w=1
test_2(3,4)

